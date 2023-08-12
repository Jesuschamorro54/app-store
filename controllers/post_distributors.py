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
    result = {'data': [], 'status': False}

    company = data['company']

    if company:

        for field, value in data.items():

            if str_validator(value):
                validation.append(1)

        if len(validation) == len(data):
            inserted = insert('distributors', data)
            result = {
                'data': inserted,
                'status': bool(inserted)
            }



        else:
            print(f"{R} * You must complete the fields properly. {RS}")

    else:
        return f"{RS} * Field 'COMPANY' is necessary to make a database register. {RS}"

    # Response
    status = result['status']

    if not status:
        result.update({
            'data': [],
            'error': "CreateException",
            'errorMessage': "Coulnt create the distributor register." 
        }) 

    return result
