from db.run_sql import run_sql

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

from models.animal import Animal


def save(animal):
    sql = "INSERT INTO animals (name, dob, species, breed, owner_id, vet_id, date_registered, checked_in) VALUES (%s, %s ,%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [
        animal.name,
        animal.dob,
        animal.species,
        animal.breed,
        animal.owner.id,
        animal.vet.id,
        animal.date_registered,
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
        owner = owner_repository.select(row["owner_id"])
        vet = vet_repository.select(row["vet_id"])
        animal = Animal(
            row["name"],
            row["dob"],
            row["species"],
            row["breed"],
            owner,
            vet,
            row["date_registered"],
            row["checked_in"],
            row["id"],
        )
    return animal


def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row["owner_id"])
        vet = vet_repository.select(row["vet_id"])
        animal = Animal(
            row["name"],
            row["dob"],
            row["species"],
            row["breed"],
            owner,
            vet,
            row["date_registered"],
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
    sql = "UPDATE animals SET (name, dob, species, breed, owner_id, vet_id, date_registered, checked_in) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        animal.name,
        animal.dob,
        animal.species,
        animal.breed,
        animal.owner.id,
        animal.vet.id,
        animal.date_registered,
        animal.checked_in,
        animal.id,
    ]
    run_sql(sql, values)


def animals_by_vet(vet):
    animals = []
    sql = "SELECT * FROM animals WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql, values)
    for row in results:
        animal = select(row["id"])
        animals.append(animal)
    return animals


def animals_by_owner(owner):
    animals = []
    sql = "SELECT * FROM animals WHERE owner_id = %s"
    values = [owner.id]
    results = run_sql(sql, values)
    for row in results:
        animal = select(row["id"])
        animals.append(animal)
    return animals
