from facili import get_data, timer
import json
import time
import datetime
import os
import psutil

DATA_DIR = ['..', 'data', 'plugins', 'resmon']


def dump_row(key, data):
    file_path = os.path.join(*(DATA_DIR + [key, str(datetime.date.today()) + '.log']))
    dir_path = os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(file_path, 'a') as f:
        data['t'] = int(time.time())
        json.dump(data, f, separators=(',',':'))
        f.write('\r\n')


"""
Collect usage data
    every 5 seconds: cpu, mem, disk_io, net_io
    every 5 minutes: disk

Split data files day-wise: 12 * 60 * 24 = 17280 entries per file
Keep past 365 days data
"""

@timer(5)
def dump_cpu_usage():
    per_cpu_percent = psutil.cpu_percent(None, True)
    loadavg = os.getloadavg()
    loadavg = (round(loadavg[0], 2), round(loadavg[1], 2), round(loadavg[2], 2))
    dump_row('cpu', {'c': per_cpu_percent, 'l': loadavg})


@timer(5)
def dump_mem_usage():
    dump_row('mem', get_data('resmon.live.mem'))


@timer(5)
def dump_disk_io_usage():
    dump_row('disk_io', get_data('resmon.live.disk_io'))


@timer(5)
def dump_net_io_usage():
    dump_row('net_io', get_data('resmon.live.net_io'))


def dump_all():
    dump_cpu_usage()
    dump_mem_usage()
    dump_disk_io_usage()
    dump_net_io_usage()



