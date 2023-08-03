from database.database import update
from controllers.validators import num_validator

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

        if num_validator(value):
            validation.append(1)

    # Condition validation
    for field, value in params.items():

        if num_validator(value):
            validation.append(1)

    if len(validation) == (len(data) + len(params)):
        result = update('details', data, params)
    
    else:
        print(f"{R}* You must complete the fields properly. {RS}")

    # Response
    return {'status': bool(result), 'data': result}


event = {
    'body': {
        'quantity': 0,
        'discount': 0,
        'total': 0
    },
    'params': {
        'order_id': 0,
        'article_id': 0
    }
}