from flask import Flask, Blueprint, render_template, request, redirect

from models.animal import Animal
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.record_repository as record_repository

animal_blueprint = Blueprint("animals", __name__)

# index
# /animals GET
@animal_blueprint.route("/animals")
def index():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", title="Animals", animals=animals)


# show
# /animals/<id> GET
@animal_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select(id)
    records = record_repository.records_by_animal(animal)
    return render_template(
        "animals/show.html", title="Animal", animal=animal, records=records,
    )


# new
# /animals/new GET
@animal_blueprint.route("/animals/new")
def new():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
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
    date_admitted = request.form["date_admitted"]
    checked_in = request.form["checked_in"]
    animal = Animal(name, dob, species, breed, owner, vet, date_admitted, checked_in)
    animal_repository.save(animal)
    return redirect("/animals")


# edit
# /animals/<id>/edit GET
@animal_blueprint.route("/animals/<id>/edit")
def edit(id):
    animal = animal_repository.select(id)
    # owners = owner_repository.select_all()
    vets = vet_repository.select_all()
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
    date_admitted = request.form["date_admitted"]
    checked_in = "checked_in" in request.form
    animal = Animal(
        name, dob, species, breed, owner, vet, date_admitted, checked_in, id
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

