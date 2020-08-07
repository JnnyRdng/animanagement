from db.run_sql import run_sql

from models.owner import Owner


def save(owner):
    sql = "INSERT INTO owners (first_name, last_name, tel, email) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [owner.first_name, owner.last_name, owner.tel, owner.email]
    id = run_sql(sql, values)[0]["id"]
    owner.id = id


def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        owner = Owner(
            row["first_name"], row["last_name"], row["tel"], row["email"], row["id"]
        )
    return owner


def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(
            row["first_name"], row["last_name"], row["tel"], row["email"], row["id"]
        )
        owners.append(owner)
    return owners


def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)


def update(owner):
    sql = "UPDATE owners SET (first_name, last_name, tel, email) = (%s, %s, %s, %s) WHERE id = %s"
    values = [owner.first_name, owner.last_name, owner.tel, owner.email, owner.id]
    run_sql(sql, values)
