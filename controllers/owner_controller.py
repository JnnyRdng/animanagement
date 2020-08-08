from flask import Flask, Blueprint, render_template, request, redirect

from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository

owner_blueprint = Blueprint("owners", __name__)


# index
# /resource GET
@owner_blueprint.route("/owners")
def index():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners=owners)


# show
# /resource/<id> GET

# new
# /resource/new GET

# create
# /resource POST

# edit
# /resource/<id>/edit GET

# update
# /resource/<id> POST

# delete
# /resource/<id>/delete POST
