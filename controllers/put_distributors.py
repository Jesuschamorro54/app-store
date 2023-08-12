from database.database import update
from controllers.validators import str_validator, bool_validator, num_validator

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

id_param_name = 'distributor_id'

def main(event):
    
    #Header
    try:
        data = event['body']
        params = {}

        if 'params' in event:
            params = event['params']

        # Get off the old var and replace it with a new one.
        if id_param_name in params:
            params['id'] = params.pop(id_param_name)

    except KeyError as e:
        return f"{R}* This method requires the params.{e}{RS}"

    # Body
    validation = []
    result = {'data': [], 'status': False}

    # Mandatory param.
    company = data['company']

    if company:

        for field, value in data.items():

            if str_validator(value):
                validation.append(1)

        # Condition validation
        for field, value in params.items():

            if num_validator(value):
                validation.append(1)

        name = params['name']
        if str_validator(name):
            validation.append(1)

        if len(validation) == (len(data) + len(params)):
            result = update('distributors', data, params)
        
    else:
        return f"{RS} * Field 'COMPANY' is necessary to update a database register. {RS}"

    # Response
    status = result['status']

    if not status:
        result.update({
            'data': [],
            'error': "UpdateException",
            'errorMessage': "Coulnt update the distributor register." 
        }) 

    return result


