from flask import Flask, Blueprint, render_template, request, redirect

from models.record import Record
import repositories.record_repository as record_repository
import repositories.animal_repository as animal_repository

record_blueprint = Blueprint("records", __name__)
nav_num = 4


# index
# /records GET
@record_blueprint.route("/records")
def index():
    records = record_repository.select_all()
    return render_template(
        "/records/index.html", nav_num=nav_num, title="Records", records=records
    )


# show
# /records/<id> GET
@record_blueprint.route("/records/<id>")
def show(id):
    record = record_repository.select(id)
    return render_template(
        "records/show.html", nav_num=nav_num, title="Record", record=record
    )


# new
# /records/new/ GET
@record_blueprint.route("/records/new")
def new():
    animals = animal_repository.select_all()
    return render_template(
        "records/new.html", nav_num=nav_num, title="New Record", animals=animals
    )


# create
# /records POST
@record_blueprint.route("/records", methods=["POST"])
def create():
    date = request.form["date"]
    entry = request.form["entry"]
    animal = animal_repository.select(request.form["animal_id"])
    record = Record(date, entry, animal)
    record_repository.save(record)
    return redirect("/records")


# edit
# /records/<id>/edit
@record_blueprint.route("/records/<id>/edit")
def edit(id):
    record = record_repository.select(id)
    return render_template(
        "/records/edit.html", nav_num=nav_num, title="Edit Record", record=record
    )


# update
# /records/<id> POST
@record_blueprint.route("/records/<id>", methods=["POST"])
def update(id):
    date = request.form["date"]
    entry = request.form["entry"]
    animal = animal_repository.select(request.form["animal_id"])
    record = Record(date, entry, animal, id)
    record_repository.update(record)
    return redirect(f"/records/{id}")


# delete
# /records/<id>/delete
@record_blueprint.route("/records/<id>/delete")
def delete(id):
    record_repository.delete(id)
    return redirect("/records")
