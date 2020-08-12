from flask import Flask, Blueprint, render_template, request, redirect

from models.owner import Owner
from models.address import Address
import repositories.owner_repository as owner_repository
import repositories.address_repository as address_repository
import repositories.animal_repository as animal_repository

owner_blueprint = Blueprint("owners", __name__)
search = False

# index
# /owners GET
@owner_blueprint.route("/owners")
def index():
    global search
    results = []
    search_term = False
    owners = owner_repository.select_all()
    if search:
        results = [
            owner
            for owner in owners
            if search.lower() in f"{owner.first_name.lower()} {owner.last_name.lower()}"
        ]
        search_term = search
        search = False

    return render_template(
        "owners/index.html",
        title="Owners",
        owners=owners,
        results=results,
        search=search_term,
    )


@owner_blueprint.route("/owners/search", methods=["POST"])
def search_results():
    global search
    search = request.form["owner_name"]
    return redirect("/owners")


# show
# /owners/<id> GET
@owner_blueprint.route("/owners/<id>")
def show(id):
    owner = owner_repository.select(id)
    animals = animal_repository.animals_by_owner(owner)
    address = owner.address.printable()
    return render_template(
        "owners/show.html", title="Owner", owner=owner, animals=animals, address=address
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
    num = request.form["num"]
    street = request.form["street"]
    city = request.form["city"]
    postcode = request.form["postcode"]
    address = Address(num, street, city, postcode)
    address_repository.save(address)
    tel = request.form["tel"]
    email = request.form["email"]
    owner = Owner(first_name, last_name, address, tel, email)
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
    owner = owner_repository.select(id)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    num = request.form["num"]
    street = request.form["street"]
    city = request.form["city"]
    postcode = request.form["postcode"]
    address_id = request.form["address_id"]
    address = Address(num, street, city, postcode, address_id)
    address_repository.update(address)
    tel = request.form["tel"]
    email = request.form["email"]
    owner = Owner(first_name, last_name, address, tel, email, owner.bill, id)
    owner_repository.update(owner)
    return redirect(f"/owners/{id}")


# # delete
# # /owners/<id>/delete POST
# @owner_blueprint.route("/owners/<id>/delete")
# def delete(id):
#     owner_repository.delete(id)
#     return redirect("/owners")
