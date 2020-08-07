from db.run_sql import run_sql

from models.vet import Vet


def save(vet):
    sql = "INSERT INTO vets (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [vet.first_name, vet.last_name]
    id = run_sql(sql, values)[0]["id"]
    vet.id = id


def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        vet = Vet(row["first_name"], row["last_name"], row["id"])
    return vet


def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row["first_name"], row["last_name"], row["id"])
        vets.append(vet)
    return vets


def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)


def update(vet):
    sql = "UPDATE vets SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.id]
    run_sql(sql, values)
