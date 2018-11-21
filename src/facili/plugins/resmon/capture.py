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


from facili import get_data, at_interval, at_time
from capture_impl import *


def get_key_data(key):
    return get_data(key).get(key)


@check_interval('cpu')
def log_cpu_usage():
    cpu = get_key_data('resmon.live.cpu')
    load = get_key_data('resmon.live.load')
    log_row('cpu', {'pc': cpu['per_cpu'], 'ac': cpu['avg'], 'l': load[0]})


@check_interval('mem')
def log_mem_usage():
    mem = get_key_data('resmon.live.mem')
    log_row('mem', {'a': mem.get('available') / 1024 ** 2,
                     'f': mem.get('free') / 1024 ** 2,
                     'u': mem.get('used') / 1024 ** 2,
                     'p': mem.get('percent')})


@check_interval('disk')
def log_disk_usage():
    du = get_key_data('resmon.live.disk')
    disk = {}
    for d in du:
        if 'used' in du[d] and 'free' in du[d] and 'percent' in du[d]:
            disk[d] = {'u': du[d]['used'] / 1024 ** 2,
                       'f': du[d]['free'] / 1024 ** 2,
                       'p': du[d]['percent']}
    log_row('disk', disk)


@check_interval('disk_io')
def log_disk_io_usage():
    dio = get_key_data('resmon.live.disk_io')
    disk_io = {}
    for d in dio:
        r, w = dio[d].get('read_speed') or 0, dio[d].get('write_speed') or 0
        if r + w:
            disk_io[d] = {'r': r, 'w': w}
    log_row('disk_io', disk_io)


@check_interval('net_io')
def log_net_io_usage():
    nio = get_key_data('resmon.live.net_io')
    net_io = {}
    for n in nio:
        r, s = nio[n].get('recv_speed') or 0, nio[n].get('send_speed') or 0
        if r + s:
            net_io[n] = {'r': r, 's': s}
    log_row('net_io', net_io)


@check_interval('top5')
def log_net_io_usage():
    top5 = get_key_data('resmon.live.top5')
    log_row('top5', top5)


@at_interval(1)
def log_all():
    log_cpu_usage()
    log_mem_usage()
    log_disk_usage()
    log_disk_io_usage()
    log_net_io_usage()


@at_interval(3600)
def logs_housekeeping():
    cleanup_old_logs()

