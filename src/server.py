from bottle import route, request, response, run
from facili import get_data


@route('/data')
def serve_data():
    k = request.query.get('k')
    keys = k.split(',') if k else [] 
    return get_data(keys)


run(host='0.0.0.0', port=8888, server='twisted')
