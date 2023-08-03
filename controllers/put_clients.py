from database.database import update
from controllers.validators import str_validator, bool_validator, num_validator

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

def main(event):
    
    #Header
    try:
        data = event['body']
        params = {}

        if 'params' in event:
            params = event['params']

    except KeyError as e:
        return f"{R}* This method requires the params.{e}{RS}"

    # Body
    validation = []
    result = {}

    for field, value in data.items():

        if str_validator(value):
            validation.append(1)

    favorite = data['favorite']
    if bool_validator(favorite):
        validation.append(1)

    # Condition validation
    for field, value in params.items():

        if num_validator(value):
            validation.append(1)

    if len(validation) == (len(data) + len(params)):
        result = update('clients', data, params)
    
    else:
        print(f"{R}* You must complete the fields properly. {RS}")

    # Response
    return {'status': bool(result), 'data': result}


event = {
    'body': {
        'name': "",
        'cellphone': "",
        'email': "",
        'favorite': None
    },
    'params': {
        'id': 0
    },
    'user': {}
}