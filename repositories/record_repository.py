from db.run_sql import run_sql

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository

from models.record import Record


def save(record):
    sql = (
        "INSERT INTO records (date, entry, animal_id) VALUES (%s, %s, %s) RETURNING id"
    )
    values = [record.date, record.entry, record.animal.id]
    id = run_sql(sql, values)[0]["id"]
    record.id = id


def select(id):
    record = None
    sql = "SELECT * FROM records WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        animal = animal_repository.select(row["animal_id"])
        record = Record(row["date"], row["entry"], animal, row["id"])
    return record


def select_all():
    records = []
    sql = "SELECT * FROM records"
    results = run_sql(sql)
    for row in results:
        animal = animal_repository.select(row["id"])
        record = Record(row["date"], row["entry"], animal, row["id"])
        records.append(record)
    return records


def delete(id):
    sql = "DELETE FROM records WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM records"
    run_sql(sql)


def update(record):
    sql = "UPDATE records SET (date, entry, animal_id) = (%s, %s, %s) WHERE id = %s"
    values = [record.date, record.entry, record.animal.id, record.id]
    run_sql(sql, values)
