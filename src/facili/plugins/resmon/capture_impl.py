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


CAPTURE_INTERVALS = {
    'cpu': 5,
    'mem': 10,
    'disk': 60,
    'disk_io': 5,
    'net_io': 5
}

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
        CAPTURE_INTERVALS.update({ key: int(val) for key, val in cfg.items('capture_interval') })
    except ConfigParser.NoSectionError, err:
        pass


read_config()

last_log_time = { key : time.time() for key in CAPTURE_INTERVALS }

def check_interval(key):
    global last_log_time
    def check_interval_decorator(func):
        def func_wrapper():
            t = time.time()
            if (t - last_log_time[key]) >= CAPTURE_INTERVALS[key]:
                func()
                last_log_time[key] += CAPTURE_INTERVALS[key]
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
        data['t'] = int(time.time())
        json.dump(data, f, separators=(',',':'))
        f.write('\r\n')
