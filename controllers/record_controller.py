from flask import Flask, Blueprint, render_template, request, redirect
import datetime

from models.record import Record
from models.date_helper import DateHelper

import repositories.record_repository as record_repository
import repositories.animal_repository as animal_repository

record_blueprint = Blueprint("records", __name__)


# index
# /records GET
@record_blueprint.route("/records")
def index():
    records = record_repository.select_all()
    return render_template("/records/index.html", title="Records", records=records)


# show
# /records/<id> GET
@record_blueprint.route("/records/<id>")
def show(id):
    record = record_repository.select(id)
    return render_template("records/show.html", title="Record", record=record)


# new
# /records/new/ GET
@record_blueprint.route("/records/new")
@record_blueprint.route("/records/new/<animal_id>")
def new(animal_id=None):
    animal = None
    animals = []
    if animal_id is not None:
        animal = animal_repository.select(animal_id)
    else:
        animals = animal_repository.select_all()
    dh = DateHelper()
    current_time = dh.print_datetime_local(datetime.datetime.now())
    return render_template(
        "records/new.html",
        title="New Record",
        animals=animals,
        animal=animal,
        current_time=current_time,
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
    return render_template("/records/edit.html", title="Edit Record", record=record)


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
