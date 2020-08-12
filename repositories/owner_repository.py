from db.run_sql import run_sql

from models.owner import Owner

import repositories.address_repository as address_repository


def save(owner):
    sql = "INSERT INTO owners (first_name, last_name, address_id, tel, email, bill) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [
        owner.first_name,
        owner.last_name,
        owner.address.id,
        owner.tel,
        owner.email,
        owner.bill,
    ]
    id = run_sql(sql, values)[0]["id"]
    owner.id = id


def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        address = address_repository.select(row["address_id"])
        owner = Owner(
            row["first_name"],
            row["last_name"],
            address,
            row["tel"],
            row["email"],
            row["bill"],
            row["id"],
        )
    return owner


def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        address = address_repository.select(row["address_id"])
        owner = Owner(
            row["first_name"],
            row["last_name"],
            address,
            row["tel"],
            row["email"],
            row["bill"],
            row["id"],
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
    sql = "UPDATE owners SET (first_name, last_name, address_id, tel, email, bill) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        owner.first_name,
        owner.last_name,
        owner.address.id,
        owner.tel,
        owner.email,
        owner.bill,
        owner.id,
    ]
    run_sql(sql, values)
