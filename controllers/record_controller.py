from flask import Flask, Blueprint, render_template, request, redirect
import datetime

from models.record import Record
from models.date_helper import DateHelper

import repositories.record_repository as record_repository
import repositories.animal_repository as animal_repository

record_blueprint = Blueprint("records", __name__)


@record_blueprint.route("/records/<id>")
def show(id):
    record = record_repository.select(id)
    return render_template("records/show.html", title="Record", record=record)


@record_blueprint.route("/records/new/<animal_id>")
def new(animal_id):
    animal = animal_repository.select(animal_id)
    dh = DateHelper()
    current_time = dh.print_datetime_local(datetime.datetime.now())
    return render_template(
        "records/new.html",
        title="New Record",
        animal=animal,
        current_time=current_time,
    )


@record_blueprint.route("/records", methods=["POST"])
def create():
    date = request.form["date"]
    entry = request.form["entry"]
    animal = animal_repository.select(request.form["animal_id"])
    record = Record(date, entry, animal)
    record_repository.save(record)
    return redirect(f"/animals/{request.form['animal_id']}")


@record_blueprint.route("/records/<id>/edit")
def edit(id):
    record = record_repository.select(id)
    return render_template("/records/edit.html", title="Edit Record", record=record)


@record_blueprint.route("/records/<id>", methods=["POST"])
def update(id):
    date = request.form["date"]
    entry = request.form["entry"]
    animal = animal_repository.select(request.form["animal_id"])
    record = Record(date, entry, animal, id)
    record_repository.update(record)
    return redirect(f"/records/{id}")


@record_blueprint.route("/records/<id>/delete")
def delete(id):
    record = record_repository.select(id)
    animal_id = record.animal.id
    record_repository.delete(id)
    return redirect(f"/animals/{animal_id}")
