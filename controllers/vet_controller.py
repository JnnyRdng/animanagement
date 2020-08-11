from flask import Flask, Blueprint, render_template, request, redirect

from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

vet_blueprint = Blueprint("vets", __name__)
search = False

# index
# /vets GET
@vet_blueprint.route("/vets")
def index():
    global search
    results = []
    search_term = False
    vets = vet_repository.select_all()
    if search:
        results = [
            vet
            for vet in vets
            if search.lower() in f"{vet.first_name.lower()} {vet.last_name.lower()}"
        ]
        search_term = search
        search = False

    return render_template(
        "/vets/index.html", title="Vets", vets=vets, results=results, search=search_term
    )


@vet_blueprint.route("/vets/search", methods=["POST"])
def search_results():
    global search
    search = request.form["vet_name"]
    return redirect("/vets")


# show
# /vets/<id> GET
@vet_blueprint.route("/vets/<id>")
def show(id):
    vet = vet_repository.select(id)
    animals = animal_repository.animals_by_vet(vet)
    count = len(animals)
    vet.set_count(count)
    if vet.animal_count >= vet.max_animals:
        vet.set_busy()

    return render_template("/vets/show.html", title="Vet", vet=vet, animals=animals)


# new
# /vets/new GET
@vet_blueprint.route("/vets/new")
def new():
    return render_template("/vets/new.html", title="Hire Vet")


# create
# /vets POST
@vet_blueprint.route("/vets", methods=["POST"])
def create():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    max_animals = request.form["max_animals"]
    vet = Vet(first_name, last_name, max_animals)
    vet_repository.save(vet)
    return redirect("/vets")


# edit
# /vets/<id>/edit GET
@vet_blueprint.route("/vets/<id>/edit")
def edit(id):
    vet = vet_repository.select(id)
    return render_template("vets/edit.html", title="Edit Vet", vet=vet)


# update
# /vets/<id> POST
@vet_blueprint.route("/vets/<id>", methods=["POST"])
def update(id):
    # vet = vet_repository.select(id)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    max_animals = request.form["max_animals"]
    vet = Vet(first_name, last_name, max_animals, id)
    vet_repository.update(vet)
    return redirect(f"/vets/{id}")


# # delete
# # /vets/<id>/delete POST
# @vet_blueprint.route("/vets/<id>/delete")
# def delete(id):
#     vet_repository.delete(id)
#     return redirect("/vets")
