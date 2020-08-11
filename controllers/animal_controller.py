from flask import Flask, Blueprint, render_template, request, redirect
import datetime

from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.record_repository as record_repository
import repositories.treatment_repository as treatment_repository

animal_blueprint = Blueprint("animals", __name__)
search = False

# index
# /animals GET
@animal_blueprint.route("/animals")
def index():
    global search
    results = []
    search_term = False
    animals = animal_repository.select_all()
    if search:
        results = [
            animal for animal in animals if search.lower() in animal.name.lower()
        ]
        for result in results:
            treatment = treatment_repository.select(result)
            result.where(treatment)
        search_term = search
        search = False
    for animal in animals:
        treatment = treatment_repository.select(animal)
        animal.where(treatment)

    return render_template(
        "animals/index.html",
        title="Animals",
        animals=animals,
        results=results,
        search=search_term,
    )


@animal_blueprint.route("/animals/admitted")
def admitted():
    animals = animal_repository.select_all()
    for animal in animals:
        treatment = treatment_repository.select(animal)
        animal.where(treatment)
    checked_in_animals = [animal for animal in animals if animal.checked_in]
    return render_template(
        "animals/index.html", title="Animals", animals=checked_in_animals, admitted=True
    )


@animal_blueprint.route("/animals/search", methods=["POST"])
def search_results():
    global search
    search = request.form["animal_name"]
    return redirect("/animals")


# show
# /animals/<id> GET
@animal_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select(id)
    treatment = treatment_repository.select(animal)
    animal.where(treatment)
    if not animal.checked_in and treatment is not None:
        treatment_repository.delete(treatment.id)
        treatment = None
    records = record_repository.records_by_animal(animal)
    return render_template(
        "animals/show.html",
        title="Animal",
        animal=animal,
        records=records,
        treatment=treatment,
    )


# new
# /animals/new GET
@animal_blueprint.route("/animals/new")
def new():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    for vet in vets:
        count = animal_repository.assigned_to(vet)
        vet.set_count(count)
        if vet.animal_count >= vet.max_animals:
            vet.set_busy()
        else:
            vet.set_available()
    return render_template(
        "/animals/new.html", title="Register Animal", owners=owners, vets=vets,
    )


# create
# /animals POST
@animal_blueprint.route("/animals", methods=["POST"])
def create():
    name = request.form["name"]
    dob = request.form["dob"]
    species = request.form["species"]
    breed = request.form["breed"]
    owner = owner_repository.select(request.form["owner_id"])
    vet = vet_repository.select(request.form["vet_id"])
    date_registered = datetime.datetime.now()
    # date_registered = request.form["date_registered"]
    checked_in = "checked_in" in request.form
    animal = Animal(name, dob, species, breed, owner, vet, date_registered, checked_in)
    animal_repository.save(animal)
    return redirect(f"/animals/{animal.id}")


# edit
# /animals/<id>/edit GET
@animal_blueprint.route("/animals/<id>/edit")
def edit(id):
    animal = animal_repository.select(id)
    # owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    for vet in vets:
        count = animal_repository.assigned_to(vet)
        vet.set_count(count)
        if vet.animal_count >= vet.max_animals and animal.vet.id is not vet.id:
            vet.set_busy()
        else:
            vet.set_available()
    return render_template(
        "animals/edit.html",
        title="Edit Animal",
        animal=animal,
        # owners=owners,
        vets=vets,
    )


# update
# /animals/<id> POST
@animal_blueprint.route("/animals/<id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    dob = request.form["dob"]
    species = request.form["species"]
    breed = request.form["breed"]
    owner = owner_repository.select(request.form["owner_id"])
    vet = vet_repository.select(request.form["vet_id"])
    date_registered = request.form["date_registered"]
    checked_in = "checked_in" in request.form
    animal = Animal(
        name, dob, species, breed, owner, vet, date_registered, checked_in, id
    )
    animal_repository.update(animal)
    return redirect(f"/animals/{id}")


# delete
# /animals/<id>/delete POST
@animal_blueprint.route("/animals/<id>/delete")
def delete(id):
    animal_repository.delete(id)
    return redirect("/animals")


# check_out
# /animals/<id>/checkout POST
@animal_blueprint.route("/animals/<id>/checkout")
def checkout(id):
    animal = animal_repository.select(id)
    animal.check_out()
    animal_repository.update(animal)
    return redirect(f"/animals/{id}")

