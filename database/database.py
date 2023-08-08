import pymysql
from .connection_db import execute_query

# Colors
R = '\033[31m'  # Red
G = '\033[32m'  # Green
RS = '\033[39m'  # Reset

def build_query(query: str, val, val2, types: tuple, status: int = 0):
    """
    build_query
    ----
    This method create a query endpoint taking the conditions and the original
    sentence (query) given. Verify the type of a value in the sentence and
    concatenates the sentence given with the endpoint. Returns the new query.

    Params:
    * query: The original sentence.
    * val: The first value, also it can be used as a 'key'.
    * val2: The second value, this can be a numtype.
    * types: Receives a tuple to use in the method 'isintance'. 
    * status: Defines if the query is for an update method or else.

    Status Index:
    * 0: Update method.
    * 1: Select method.
    * 2: Insert method.

    """

    if status == 0:
        if isinstance(val2, (types)):
            query += f"{val} = {val2}"

        else:
            query += f'{val} = "{val2}"'

    elif status == 1:
        if isinstance(val2, (types)):
            query += f"{val} = {val2}"

        else:
            query += f'{val} LIKE "%{val2}%"'

    elif status == 2:

        if isinstance(val[val2], (types)):
            query += f"{val[val2]}, "

        else:
            query += f'"{val[val2]}", '

    else:
        print(f"{R}* STATUS ONLY RECIEVES STATUS FROM 0 TO 2 (one digit).{RS}")

    return query


def insert(table: str, data: dict):
    """
    insert
    -----

    This method simulates an INSERT query from MySql using the keys and the data to create 
    a functional and scalable sentence. Returns the query.

    Params:
    * table: Receives the name of the table where the query will be insert.
    * data: Receives a dictionary with the name of the key and its respective value.

    """
    query = f"INSERT INTO {table} ("

    # PUT KEYS
    for key in data:

        query += f"{key}, "

    # Query body
    query = query.rstrip(', ') + ") VALUES ("

    # PUT VALUES:
    for key in data:

        query = build_query(query, data, key, (int, float), 2)

    query = query.rstrip(', ') + ")"

    id = execute_query(query, True)

    if not id:
        return False

    data.update({'id': id})
    return data


def search(table, params):
    """
    search
    ----
    This method simulate the 'SELECT' method from MySql. Creates a sentence and search
    with it in the database. Can be parametrized with conditionals and logic comparators.
    Returns the query.

    Params:
    * table: The name of the table where the method will be used.
    * params: A set of params with fields and conditions.
    """

    fields = params.pop('fields', "*")
    query = f"SELECT ("

    # Init query.
    if fields != "*":

        for field in fields:

            query += f"{field}, "

        query = query[:-2] + ")"  # Strip coma and close tuple.

    else:
        query = f"SELECT {fields}"

    # End of the query head.
    query += f" FROM {table}"

    # Query conditions.
    if params:
        query += " WHERE "

        for key, value in params.items():

            query = build_query(query, key, value, (int, float), 1)

            query += " AND "

        query = query[:-4]  # Strip AND.

    else:
        query += ";"

    execute_query(query)


def update(table, field, condition):
    """
    update
    ---
    This method simulate the 'UPDATE' fucntion of MySql. Can be parametrized in its
    body with conditions, use reserved words (SET) and logic comparators. Returns teh query.

    Params:
    * table: The name of the table in the database.
    * condition: A set of conditions connected by 'AND'.
    * field: The field which will be updated by the method. 

    """

    # Init query.
    query = f"UPDATE {table} SET "

    query = build_query(query, field[0], field[1], (int, float))

    query += " WHERE "  # Start with the condition body.

    for key, value in condition.items():

        query = build_query(query, key, value, (int, float))

        query += " AND "

    # Strip AND, space and concatenate ';'.
    query = query[:-4].rstrip() + ";"  # Final query.

    execute_query(query, True)


def delete(table, condition):
    """
    delete
    ---
    This method simulates the 'DELETE' function from MySql. Requieres a mandatory
    condition or a set of them. Returns the query.

    Params:
    * table: The name of the table in the database.
    * condition: The mandatory set of conditions to delete a register in the table.

    """

    # Init query.
    query = f"DELETE FROM {table} WHERE "

    # Body condition.
    for key, value in condition.items():

        query = build_query(query, key, value, (int, float))

        query += " AND "

    # Strip AND, space and add the ";".
    query = query[:-4].rstrip() + ";"  # Final query

    return execute_query(query, True)


def close():
    pass



