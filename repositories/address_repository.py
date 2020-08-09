from db.run_sql import run_sql

from models.address import Address


def save(address):
    sql = "INSERT INTO addresses (num, street, city, postcode) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [address.num, address.street, address.city, address.postcode]
    id = run_sql(sql, values)[0]["id"]
    address.id = id


def select(id):
    address = None
    sql = "SELECT * FROM addresses WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        address = Address(row["num"], row["street"], row["city"], row["postcode"], id)
    return address


def select_all():
    addresses = []
    sql = "SELECT * FROM addresses"
    results = run_sql(sql)
    for row in results:
        address = Address(row["num"], row["street"], row["city"], row["postcode"], id)
        addresses.append(address)
    return addresses


def update(address):
    sql = "UPDATE addresses (num, street, city, postcode) = (%s, %s, %s, %s) WHERE id = %s"
    values = [
        address.num,
        address.street,
        address.city,
        address.postcode,
        address.id,
    ]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM addresses WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM addresses"
    run_sql(sql)
