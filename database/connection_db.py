import pymysql

BL = '\033[30m'  # Black
R = '\033[31m'  # Red
G = '\033[32m'  # Green
Y = '\033[33m'  # Yellow
B = '\033[34m'  # Blue
M = '\033[35m'  # Magenta
C = '\033[36m'  # Cian
W = '\033[37m'  # White
RS = '\033[39m'  # Reset


def connect_db():
    """
    Connect to database.
    """

    connection = {}
    params = {
        "host": "localhost",
        "user": "root",
        "password": "alracopo1",
        "database": "problema_1",
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor
    }

    try:
        connection = pymysql.connect(**params)
        print(f"{G} * Connection to MySQL instance done.{RS}")

    except Exception as e:
        print(f"{R} * Couldn't connect to MySQL instance: {RS}", e)

    return connection


def execute_query(query):
    """
    execute_query
    ---

    The method receives a query it is in SQL and its gonna be executed.

    params:
    * query: The query on SQL.
    """

    # SELECT.
    conn = connect_db()
    data = {}

    print(f"Query executing: {query}\n")
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)

            data = cursor.fetchall()
            print(f"{G} *The query has been executed successfully.{RS}")

    except Exception as e:
        print(f'{R} * ERROR: Could not execute SQL query.\n{RS} {e}')
