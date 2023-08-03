from database.database import search

R = '\033[31m'  # Red
RS = '\033[39m'  # Reset

def main(event):
    
    # Header
    try:
        params = event['params']
        user = {}

        if 'user' in event:
            user = event['user']

            for key, value in user.items():
                params.update({key: value})

    except KeyError as e:
        return f"{R}* The method needs the params.{RS} {e}"
    
    # Body
    result = search('clients', params)

    # Response
    return {'status': bool(result), 'data': result}

event = {
    'body': {},
    'params': {
        'distributor_id': 0,
        'cost': 0
    },
    'user': {}
}