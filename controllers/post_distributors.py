from database.database import insert
from controllers.validators import str_validator

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

def main(event):
    
    # Header
    try:
        data = event['body']
        params = {}

        if "params" in event:
            params = event['params']

            for key, value in params.items():
                data.update({key: value})

    except KeyError as e:
        return f"{R}* The method needs the params.{RS} {e}"
        
    # Body
    validation = []
    result = {}

    for field, value in data.items():

        if str_validator(value):
            validation.append(1)

    if len(validation) == len(data):
        result = insert('distributors', data)

    else:
        print(f"{R} * You must complete the fields properly. {RS}")

    # Response
    return {'status': bool(result), 'data': result}

event = {
    'body': {
        'name': "",
        'cellphone': "",
        'email': "",
        'company': ""
    },
    'params': {}
}