# facili - easy info tool framework

# Copyright (C) 2018 Siddharudh P T

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


import importlib, pkgutil
import time

plugin_data_func = {}
plugin_module_name = ''

cache_func_output = {}

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


def cache(dur=31536000000):
    global cache_func_output
    def cache_decorator(func):
        def func_wrapper():
            r = cache_func_output.get(func)
            if r and dur > (time.time() - r[1]):
                return r[0]
            output = func()
            cache_func_output[func] = output, time.time()
            return output
        return func_wrapper
    return cache_decorator


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
    p = plugin_module_name[len(PLUGINS_BASE_NAME)+1:]
    if key:
        p += '.' + key
    plugin_data_func[p] = func
    func.key = p


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

def list_plugins():
    plugins = {}
    import facili.plugins
    package = facili.plugins
    for importer, submodule, ispkg in pkgutil.iter_modules(package.__path__):
        sm = importlib.import_module('facili.plugins.' + submodule)
        plugins[submodule] = filter(None, sm.__doc__.split('\n'))
    return plugins

