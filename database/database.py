import pymysql
from connection_db import execute_query, connect_db

connection = connect_db()


def search(table, params):
    pass


def update():
    pass


def insert(table: str, values: dict):
    """
    insert
    -----

    This method simulates an INSERT query from MySql using the keys and the values to create 
    a functional and scalable sentence. Returns the query.

    params:
    * table: string. Receives the name of the table where the query will be insert.
    * values: dict. Receives a dictionary with the name of the key and its respective value.

    """
    query = f"INSERT INTO {table} ("

    # PUT KEYS
    for key in values:

        query += f"{key}, "

    query = query.rstrip(', ')

    query += ") values ("

    # PUT VALUES
    for key in values:
        query += f"'{values[key]}', "

    query = query.rstrip(', ')

    query += ")"

    return query


values = {"name": "'Alfredo'",
          "address": "'Villa Carolina'",
          "email": "'alfredocomas8@gmail.com'",
          "favorite": 1}


insert("clients", values)


def delete():
    pass


def close():
    pass


connection.commit()
connection.close()
