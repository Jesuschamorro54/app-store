from database.database import delete
from controllers.validators import str_validator, num_validator

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

        if num_validator(value):
            validation.append(1)
    
    name = params['name']
    if str_validator(name):
        validation.append(1)
    
    if len(validation) == len(params):
        result = delete('articles', params)
    
    # Response
    return {'status': bool(result), 'data': result}

event = {
    'body': {},
    'params': {
        'name': "",
        'cost': 0,
        'price': 0,
        'sale': 0,
        'stock': 0,
        'distributor_id': 0
    },
    'user': {}
}