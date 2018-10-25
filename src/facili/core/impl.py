import importlib, pkgutil


plugin_data_func = {}
plugin_module_name = ''

PLUGINS_BASE_NAME = 'facili.plugins'

def data(key):
    def data_decorator(func):
        register_plugin_data_func(key, func)
        def func_wrapper():
            if not key or type(key) != str:
                raise Exception('Invalid key')
            return func()
        return func_wrapper
    return data_decorator


def timer(seconds):
    def timer_decorator(func):
        def func_wrapper():
            if not seconds or type(seconds) != int:
                raise Exception('Invalid value for timer seconds')
            return func()
        return func_wrapper
    return timer_decorator


def build_plugin_data_functions(module):
    global plugin_module_name
    package = importlib.import_module(module)
    for importer, submodule, ispkg in pkgutil.iter_modules(package.__path__):
        plugin_module_name = module + '.' + submodule
        if ispkg:
            build_plugin_data_functions(plugin_module_name)
        else:
            importlib.import_module(plugin_module_name)


def register_plugin_data_func(key, func):
    """Registers plugin data functions"""
    global plugin_data_func
    plugin = plugin_module_name[len(PLUGINS_BASE_NAME)+1:]
    if key:
        plugin_data_func[plugin + '.' + key] = func
    else:
        plugin_data_func[plugin] = func


def get_data(keys=[]):
    """Collects data from all plugins and returns in JSON format"""
    if type(keys) == str:
        keys = [keys]
    output = {}
    for key in plugin_data_func:
        if not keys or any((key == k or key.startswith(k + '.') for k in keys)):
            if '._' not in key or key in keys:
                func = plugin_data_func[key]
                output[key] = func()
    return output
