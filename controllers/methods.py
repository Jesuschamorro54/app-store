
def build_query(query: str, val, val2, types: tuple):
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

    """

    if isinstance(val2, (types)):
        query += f"{val} = {val2}"

    else:
        query += f'{val} = "{val2}"'

    return query
