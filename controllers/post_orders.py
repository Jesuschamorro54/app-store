from database.database import insert
from controllers.validators import str_validator, num_validator
import datetime

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

def main(event):
    
    # Header
    try:
        data = event['body']
        params = {}

        # Extract extra_data.
        extra_data = data['extra_data']

        if "params" in event:
            params = event['params']

            for key, value in params.items():
                data.update({key: value})

    except KeyError as e:
        return f"{R}* The method needs the params.{RS} {e}"
        
    # Body
    validation = []
    result = {'data': [], 'status': False}

    # Mandatory params.
    total = data['total']

    # Default params.
    default = {
        'purchase_date' : datetime.datetime.now(),
        'amount' : 1
    }

    if total:

        for field, value in data.items():

            if num_validator(value):
                validation.append(1)
        
        purchase_date = data['purchase_date']
        if str_validator(purchase_date):
            validation.append(1)

        if len(validation) == len(data):
            order = insert('orders', data)

        else:
            print(f"{R} * You must complete the fields properly. {RS}")

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
                detail_inserted = insert('details', detail)
                detail.update({'id': detail_inserted['id']})

                result['data']['details'].append(detail)
    
    else:
        return f"{RS} * Field 'TOTAL' is necessary to make a database register. {RS}"

    # Response
    status = result['status']   

    if not status:
        result.update({
            'data': [],
            'error': "CreateException",
            'errorMessage': "Coulnt create the order register." 
        }) 

    return result

