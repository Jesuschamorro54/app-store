from database.database import search

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

id_param_name = 'order_id'

def main(event):
    
    # Header
    try:
        params = event['params']
        user = {}

        if 'user' in event:
            user = event['user']

            for key, value in user.items():
                params.update({key: value})
        
        # Get off the old var and replace it with a new one.
        if id_param_name in params:
            params['id'] = params.pop(id_param_name)

    except KeyError as e:
        return f"{R}* The method needs the params.{RS} {e}"
    
    # Body
    result = search('orders', params)

    # Response
    return {'status': bool(result), 'data': result}

