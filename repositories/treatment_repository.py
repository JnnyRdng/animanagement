from db.run_sql import run_sql

import repositories.animal_repository as animal_repository

from models.treatment import Treatment


def save(treatment):
    sql = "INSERT INTO treatments (description, start, duration, recovery, cost, animal_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [
        treatment.description,
        treatment.start,
        treatment.duration,
        treatment.recovery,
        treatment.cost,
        treatment.animal.id,
    ]
    id = run_sql(sql, values)[0]["id"]
    treatment.id = id


def select(id):
    treatment = None
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        animal = animal_repository.select(row["animal_id"])
        treatment = Treatment(
            row["decription"],
            row["duration"],
            row["recovery"],
            row["cost"],
            animal,
            row["id"],
        )
        treatment.start = row["start"]
    return treatment


def select_all():
    treatments = []
    sql = "SELECT * FROM treatments"
    results = run_sql(sql)
    for row in results:
        animal = animal_repository.select(row["animal_id"])
        treatment = Treatment(
            row["decription"],
            row["duration"],
            row["recovery"],
            row["cost"],
            animal,
            row["id"],
        )
        treatment.start = row["start"]
        treatments.append(treatment)
    return treatments


def delete(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)


def update(treatment):
    sql = "UPDATE treatments SET (description, start, duration, recovery, cost, animal_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        treatment.description,
        treatment.start,
        treatment.duration,
        treatment.recovery,
        treatment.cost,
        treatment.animal.id,
        treatment.id,
    ]
    run_sql(sql, values)

