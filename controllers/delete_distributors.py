from database.database import delete
from controllers.validators import str_validator

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

def main(event):
    
    # Header
    try:
        params = event['params']

    except KeyError as e:
        return f"{R}* This method requires the parameters.{e}{RS}"
    
    # Body
    validation = []
    result = {}

    for field, value in params.items():

        if str_validator(value):
            validation.append(1)
    
    if len(validation) == len(params):
        result = delete('distributors', params)
    
    # Response
    return {'status': bool(result), 'data': result}

event = {
    'body': {},
    'params': {
        'name': "",
        'cellphone': "",
        'email': "",
        'company': ""
    },
    'user': {}
}