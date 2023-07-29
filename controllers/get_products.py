from database.database import search


def main(event):

    featured = search('products', {})

    new = search('products', {})

    # if featured and new:
    # return {'status': True, 'data': }
    # return {'status': bool, 'data': array}
