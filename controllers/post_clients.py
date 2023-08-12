from database.database import insert
from controllers.validators import str_validator, bool_validator

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

    name = data['name']

    if name:

        for field, value in data.items():

            if str_validator(value):
                validation.append(1)
            
        favorite = data['favorite']
        if bool_validator(favorite):
            validation.append(1)

        if len(validation) == len(data):
            inserted = insert('clients', data)
            result = {
                'data': inserted,
                'status': bool(inserted)
            }

        else:
            print(f"{R} * You must complete the fields properly. {RS}")

    else:
        return f"{RS} * Field 'NAME' is necessary to make a database register. {RS}"

    # Response
    status = result['status']

    if not status:
        result.update({
            'data': [],
            'error': "CreateException",
            'errorMessage': "Coulnt create the client register." 
        }) 

    return result


