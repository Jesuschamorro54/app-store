import pymysql
from connection_db import execute_query


def search(table, params):
    pass


def update():
    pass


def insert(table, values):  # CREATE

    # Estructura de la query
    sql = f"""INSERT INTO {table} (name, address, email, favorite) values
              ({values['name']}, {values['address']}, {values['email']}, {values['favorite']})"""

    data = execute_query(sql)
    return data


values = {"name": "'Alfredo'",
          "address": "'Villa Carolina'",
          "email": "'alfredocomas8@gmail.com'",
          "favorite": 1}


insert("clients", values)


def delete():
    pass
