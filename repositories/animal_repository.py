from db.run_sql import run_sql

import repositories.vet_repository as vet_repo
import repositories.owner_repository as owner_repo

from models.vet import Vet
from models.owner import Owner
from models.animal import Animal


def save(animal):
    sql = "INSERT INTO animals (name, dob, species, owner_id, vet_id, date_admitted, checked_in) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [
        animal.name,
        animal.dob,
        animal.species,
        animal.owner.id,
        animal.vet.id,
        animal.date_admitted,
        animal.checked_in,
    ]
    id = run_sql(sql, values)[0]["id"]
    animal.id = id


def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        owner = owner_repo.select(row["owner_id"])
        vet = vet_repo.select(row["vet_id"])
        animal = Animal(
            row["name"],
            row["dob"],
            row["species"],
            owner,
            vet,
            row["date_admitted"],
            row["checked_in"],
            row["id"],
        )
    return animal


def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        owner = owner_repo.select(row["owner_id"])
        vet = vet_repo.select(row["vet_id"])
        animal = Animal(
            row["name"],
            row["dob"],
            row["species"],
            owner,
            vet,
            row["date_admitted"],
            row["checked_in"],
            row["id"],
        )
        animals.append(animal)
    return animals


def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)


def update(animal):
    sql = "UPDATE animals SET (name, dob, species, owner_id, vet_id, date_admitted, checked_in) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        animal.name,
        animal.dob,
        animal.species,
        animal.owner.id,
        animal.vet.id,
        animal.date_admitted,
        animal.checked_in,
        animal.id,
    ]
    run_sql(sql, values)
