from flask import Flask, Blueprint, render_template, request, redirect
import datetime

from models.treatment import Treatment
from models.date_helper import DateHelper

import repositories.treatment_repository as treatment_repository
import repositories.animal_repository as animal_repository

treatment_blueprint = Blueprint("treatments", __name__)

# don't need index


@treatment_blueprint.route("/treatments/<id>")
def show(id):
    treatment = treatment_repository.select(id)
    return render_template(
        "treatments/show.html", title="Treatment", treatment=treatment
    )


@treatment_blueprint.route("/treatments/new/<animal_id>")
def new(animal_id):
    animal = animal_repository.select(animal_id)
    return render_template("treatments/new.html", title="New Treatment", animal=animal)


@treatment_blueprint.route("/treatments", methods=["POST"])
def create():
    description = request.form["description"]
    duration = request.form["duration"]
    recovery = request.form["recovery"]
    cost = request.form["cost"]
    animal = animal_repository.select(request.form["animal_id"])
    treatment = Treatment(description, duration, recovery, cost, animal)
    treatment_repository.save(treatment)
    return redirect(f"animals/{animal.id}")


@treatment_blueprint.route("/treatments/<id>/edit")
def edit(id):
    treatment = treatment_repository.select(id)
    return render_template(
        "treatments/edit.html", title="Edit Treatment", treatment=treatment
    )


@treatment_blueprint.route("/treatments/<id>", methods=["POST"])
def update(id):
    description = request.form["description"]
    duration = request.form["duration"]
    recovery = request.form["recovery"]
    cost = request.form["cost"]
    animal = animal_repository.select(request.form["animal_id"])
    treatment = Treatment(description, duration, recovery, cost, animal, id)
    treatment_repository.update(treatment)
    return redirect(f"animals/{animal.id}")


@treatment_blueprint.route("/treatments/<id>/delete")
def delete(id):
    treatment = treatment_repository.select(id)
    treatment_repository.delete(id)
    return redirect(f"animals/{treatment.animal.id}")
