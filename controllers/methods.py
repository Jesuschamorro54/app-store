
from colors import R, RS


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

        if isinstance(val[val2, (types)]):
            query += f"{val[val2]}, "

        else:
            query += f'"{val[val2]}", '

    else:
        print(f"{R}* STATUS ONLY RECIEVES STATUS FROM 0 TO 1 (one digit).{RS}")

    return query
