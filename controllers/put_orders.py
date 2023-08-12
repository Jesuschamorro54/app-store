from database.database import update
from controllers.validators import str_validator, bool_validator, num_validator

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

id_param_name = "order_id"

def main(event):
     
    #Header
    try:
        data = event['body']
        params = {}

        # Extract extra_data.
        extra_data = data['extra_data']

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
    total = data['total']

    if total:

        for field, value in data.items():

            if num_validator(value):
                validation.append(1)

        purchase_date = data['purchase_date']
        if str_validator(purchase_date):
            validation.append(1)

        # Condition validation
        for field, value in params.items():

            if num_validator(value):
                validation.append(1)

        if len(validation) == (len(data) + len(params)):
            order = update('orders', data, params)
        
        else:
            print(f"{R}* You must complete the fields properly. {RS}")

        # Extract details fields.
        details = extra_data['details']
        
        if order:

            result = {
                'status': True,
                'data': {
                    **order,
                    'details': []
                }
            }

            for detail in details:

                detail.update({'order_id': order['id']})
                detail_inserted = update('details', detail)
                detail.update({'id': detail_inserted['id']})

                result['data']['details'].append(detail)

    else:
        return f"{RS} * Field 'TOTAL' is necessary to update a database register. {RS}"

    # Response
    status = result['status']

    if not status:
        result.update({
            'data': [],
            'error': "UpdateException",
            'errorMessage': "Coulnt update the order register." 
        }) 

    return result



