from flask import Flask, Blueprint, render_template, request, redirect

from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository

owner_blueprint = Blueprint("owners", __name__)

# index
# /owners GET
@owner_blueprint.route("/owners")
def index():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", title="Owners", owners=owners)


# show
# /owners/<id> GET
@owner_blueprint.route("/owners/<id>")
def show(id):
    owner = owner_repository.select(id)
    animals = animal_repository.animals_by_owner(owner)
    return render_template(
        "owners/show.html", title="Owner", owner=owner, animals=animals
    )


# new
# /owners/new GET
@owner_blueprint.route("/owners/new")
def new():
    return render_template("/owners/new.html", title="Register Owner")


# create
# /owners POST
@owner_blueprint.route("/owners", methods=["POST"])
def create():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    tel = request.form["tel"]
    email = request.form["email"]
    owner = Owner(first_name, last_name, tel, email)
    owner_repository.save(owner)
    return redirect("/owners")


# edit
# /owners/<id>/edit GET
@owner_blueprint.route("/owners/<id>/edit")
def edit(id):
    owner = owner_repository.select(id)
    return render_template("owners/edit.html", title="Edit Owner", owner=owner)


# update
# /owners/<id> POST
@owner_blueprint.route("/owners/<id>", methods=["POST"])
def update(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    tel = request.form["tel"]
    email = request.form["email"]
    owner = Owner(first_name, last_name, tel, email, id)
    owner_repository.update(owner)
    return redirect(f"/owners/{id}")


# # delete
# # /owners/<id>/delete POST
# @owner_blueprint.route("/owners/<id>/delete")
# def delete(id):
#     owner_repository.delete(id)
#     return redirect("/owners")
