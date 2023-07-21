import pymysql
from connection_db import execute_query, connect_db

connection = connect_db()


def search(table, params):
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

        if isinstance(values[key], (str)):  # String type
            query += f"'{values[key]}', "

        else:
            query += f"{values[key]}, "

    query = query.rstrip(', ')

    query += ")"

    return query


def select(table, params):

    fields = params.pop('fields', "*")
    query = f"SELECT ("

    if fields != "*":

        for field in fields:

            query += f"{field}, "

        query = query[:-2]  # Strip coma.
        query += ")"

    else:
        query = f"SELECT {fields}"

    query += f" FROM {table}"

    # Conditions of the query.
    if params['condition']:
        query += " WHERE "

        for key, value in params['condition'].items():

            # Verify if its numtype or something else.
            if isinstance(value, (int, float)):
                sentence = f'{key} = {value} AND '

            else:
                sentence = f'{key} LIKE "%{value}%" AND '

            query += sentence

        query = query[:-4]  # Strip AND.

    else:
        query += ";"

    return query


def update(table, params):

    condition = params.pop('condition', None)
    query = f"UPDATE {table}\nSET "

    field = params['field']

    if isinstance(field[1], (int, float)):
        query += f'{field[0]} = {field[1]}'

    else:
        query += f'{field[0]} = "{field[1]}"'

    # Verify if the query has a condition.
    if condition:

        query += " WHERE "

        for key, value in condition.items():

            if isinstance(value, (int, float)):
                query += f"{key} = {value} AND "

            else:
                query += f'{key} = "{value}" AND '

        query = query[:-4]  # Strip AND

    query = query.rstrip()
    query += ";"

    return query


def delete():
    pass


def close():
    pass


connection.commit()
connection.close()
