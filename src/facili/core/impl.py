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
import threading


################## Decorators ##################

def data(key):
    def data_decorator(func):
        register_plugin_data_func(key, func)
        return func
    return data_decorator


def cache(dur=31536000000):
    global cache_func_output
    def cache_decorator(func):
        def func_wrapper():
            if not hasattr(func, 'r') or not hasattr(func, 't') or (time.time() - func.t) > dur:
                func.r = func()
                func.t = time.time()
            return func.r
        return func_wrapper
    return cache_decorator


def at_interval(seconds):
    if type(seconds) not in (int, float) or seconds <= 0:
        raise Exception('Invalid at_interval seconds')
    def at_interval_decorator(func):
        register_timer_func(func, seconds)
        return func
    return at_interval_decorator


def at_time(h, m, s):
    try:
        time.strptime('%d:%d:%d' % (h, m, s), '%H:%M:%S')
    except:
        raise Exception('Invalid at_time time')
    def at_time_decorator(func):
        register_timer_func(func, (h, m, s))
        return func
    return at_time_decorator


################## Implementation ##################

plugin_data_func = {}
plugin_module_name = ''

PLUGINS_BASE_NAME = 'facili.plugins'


def build_plugin_data_functions(module):
    global plugin_module_name
    package = importlib.import_module(module)
    for importer, submodule, ispkg in pkgutil.iter_modules(package.__path__):
        if submodule.startswith('.') or submodule.startswith('_'):
            continue
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


timer_func = []
last_exec_time = {}


def register_timer_func(func, tval):
    global timer_func
    timer_func.append((func, tval))


def timer_thread_exec():
    while True:
        t = time.time()
        for func, tval in timer_func:
            if type(tval) in (int, float):
                if (t - last_exec_time.get(func, 0)) >= tval:
                    func()
                    last_exec_time[func] = last_exec_time.get(func, t) + tval
            elif type(tval) == tuple and len(tval) == 3:
                now = time.strftime('%H:%M:%S', time.localtime(t))
                sched = '%02d:%02d:%02d' % tval
                if now == sched and t - last_exec_time.get(func, 0) > 1:
                    func()
                    last_exec_time[func] = t
        time.sleep(0.1)


timer_thread = threading.Thread(target=timer_thread_exec)
timer_thread.daemon = True

def start_timer_thread():
    global timer_thread
    timer_thread.start()


def get_data(keys=[], query={}):
    """Collects data from all plugins and returns in JSON format"""
    if type(keys) == str:
        keys = [keys]
    set_query(query)
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
        if submodule.startswith('.') or submodule.startswith('_'):
            continue
        sm = importlib.import_module('facili.plugins.' + submodule)
        plugins[submodule] = filter(None, sm.__doc__.split('\n'))
    return plugins


_local_store = threading.local()


def set_query(query):
    global _local_store
    _local_store.query = query


def get_query():
    global _local_store
    if hasattr(_local_store, 'query'):
        return _local_store.query or {}
    return {}

