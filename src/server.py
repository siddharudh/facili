from bottle import route, view, request, response, static_file, template, run
import bottle
from facili import get_data, list_plugins


bottle.TEMPLATE_PATH = ['../web/templates']

@route('/data')
def serve_data():
    k = request.query.get('k')
    keys = k.split(',') if k else [] 
    return get_data(keys)


@route('/static/<path:path>')
def  serve_static_content(path):
    return static_file(path, root='../web/static')


@route('/')
@view('index')
def serve_view():
    return {'plugins': list_plugins()}


run(host='0.0.0.0', port=8888, server='twisted', debug=True)
