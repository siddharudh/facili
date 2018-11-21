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

RESOURCE_TYPES = ('cpu', 'mem', 'disk', 'disk_io', 'net_io', 'top5')

CAPTURE_INTERVAL = {
    'cpu': 60,
    'mem': 60,
    'disk': 300,
    'disk_io': 60,
    'net_io': 60,
    'top5': 60
}

MAX_LOG_SIZE = {}
MAX_LOG_DAYS = {}

DEFAULT_MAX_LOG_SIZE = 150      # MB
DEFAULT_MAX_LOG_DAYS = 365      # days

import os
import json
import time
import datetime
import ConfigParser


DATA_DIR = ['..', 'data', 'plugins', 'resmon']
CONF_DIR = ['..', 'conf']

def read_config():
    cfg = ConfigParser.ConfigParser()
    cfg.read(os.path.join(*(CONF_DIR + ['resmon.conf'])))
    try:
        default = None
        if cfg.has_option('capture_interval', '*'):
            default = cfg.getint('capture_interval', '*')
        for key in RESOURCE_TYPES:
            if cfg.has_option('capture_interval', key):
                CAPTURE_INTERVAL[key] = cfg.getint('capture_interval', key)
            elif default:
                CAPTURE_INTERVAL[key] = default
    except ConfigParser.NoSectionError, err:
        pass
    try:
        default = None
        if cfg.has_option('max_log_size', '*'):
            default = cfg.getint('max_log_size', '*')
        for key in RESOURCE_TYPES:
            if cfg.has_option('max_log_size', key):
                MAX_LOG_SIZE[key] = cfg.getint('max_log_size', key)
            elif default:
                MAX_LOG_SIZE[key] = default
            else:
                MAX_LOG_SIZE[key] = DEFAULT_MAX_LOG_SIZE
    except ConfigParser.NoSectionError, err:
        pass
    try:
        default = None
        if cfg.has_option('max_log_days', '*'):
            default = cfg.getint('max_log_days', '*')
        for key in RESOURCE_TYPES:
            if cfg.has_option('max_log_days', key):
                MAX_LOG_DAYS[key] = cfg.getint('max_log_days', key)
            elif default:
                MAX_LOG_DAYS[key] = default
            else:
                MAX_LOG_DAYS[key] = DEFAULT_MAX_LOG_DAYS
    except ConfigParser.NoSectionError, err:
        pass


read_config()

last_log_time = { key : time.time() for key in CAPTURE_INTERVAL }

def check_interval(key):
    global last_log_time
    def check_interval_decorator(func):
        def func_wrapper():
            t = time.time()
            if (t - last_log_time[key]) >= CAPTURE_INTERVAL[key]:
                func()
                last_log_time[key] += CAPTURE_INTERVAL[key]
        return func_wrapper
    return check_interval_decorator


def log_row(key, data):
    if not data:
        return
    file_path = os.path.join(*(DATA_DIR + [key, str(datetime.date.today()) + '.log']))
    dir_path = os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(file_path, 'a') as f:
        data['t'] = int(round(time.time()))
        json.dump(data, f, separators=(',',':'))
        f.write('\r\n')


def cleanup_old_logs():
    pass