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


from facili import data, cache, human_readable_size
from collections import OrderedDict
import psutil
import os
import time


@data('cpu')
@cache(2)
def cpu_usage():
    per_cpu_percent = psutil.cpu_percent(None, True)
    return {
        'per_cpu': per_cpu_percent,
        'avg': round(sum(per_cpu_percent) / len(per_cpu_percent), 2)
    }

@data('load')
@cache(5)
def current_load():
    one, five, fifteen = os.getloadavg()
    return [round(one, 2), round(five, 2), round(fifteen, 2)]


@data('mem')
@cache(10)
def mem_usage():
    return vars(psutil.virtual_memory())


@data('swap')
@cache(60)
def swap_usage():
    return vars(psutil.swap_memory())


@data('disk')
@cache(60)
def disk_usage():
    usage = OrderedDict()
    for dp in psutil.disk_partitions():
        du = psutil.disk_usage(dp.mountpoint)
        usage[dp.mountpoint] = vars(du)
    return usage


def disk_io_usage():
    usage = OrderedDict()
    dio = psutil.disk_io_counters(True)
    for d in dio:
        usage[d] = vars(dio[d])
    read_speed = write_speed = 0
    try:
        if hasattr(disk_io_usage, 't') and hasattr(disk_io_usage, 'r'):
            t = time.time()
            total_read_bytes = total_write_bytes = 0
            for d in disk_io_usage.r:
                if d == 'total':
                    continue
                read_bytes = usage[d]['read_bytes'] - disk_io_usage.r[d]['read_bytes']
                write_bytes = usage[d]['write_bytes'] - disk_io_usage.r[d]['write_bytes']
                usage[d]['read_speed'] = int(read_bytes / (t - disk_io_usage.t))
                usage[d]['write_speed'] = int(write_bytes / (t - disk_io_usage.t))
                total_read_bytes += read_bytes
                total_write_bytes += write_bytes
            usage['total'] = {
                'read_speed': int(total_read_bytes / (t - disk_io_usage.t)),
                'write_speed': int(total_write_bytes / (t - disk_io_usage.t))
            }
    except:
        pass
    return usage

disk_io_usage_wrapped = data('disk_io')(cache(2)(disk_io_usage))


def net_io_usage():
    usage = OrderedDict()
    nio = psutil.net_io_counters(True)
    for n in nio:
        usage[n] = vars(nio[n])
    try:
        if hasattr(net_io_usage, 't') and hasattr(net_io_usage, 'r'):
            t = time.time()
            total_recv_bytes = total_sent_bytes = 0
            for d in net_io_usage.r:
                if d == 'total':
                    continue
                bytes_sent = usage[d]['bytes_sent'] - net_io_usage.r[d]['bytes_sent']
                bytes_recv = usage[d]['bytes_recv'] - net_io_usage.r[d]['bytes_recv']
                usage[d]['send_speed'] = int(bytes_sent / (t - net_io_usage.t))
                usage[d]['recv_speed'] = int(bytes_recv / (t - net_io_usage.t))
                total_sent_bytes += bytes_sent
                total_recv_bytes += bytes_recv
            usage['total'] = {
                'send_speed': int(total_sent_bytes / (t - net_io_usage.t)),
                'recv_speed': int(total_recv_bytes / (t - net_io_usage.t))
            }
    except:
        raise
        pass
    return usage

net_io_usage_wrapped = data('net_io')(cache(2)(net_io_usage))


@data('top5cpu')
@cache(10)
def top5_cpu():
    data = [(p.pid, p.info['name'], round(p.info['cpu_percent'] or 0.0, 2), p.info['num_threads']) for p in sorted(psutil.process_iter(attrs=['name', 'cpu_percent', 'cpu_times', 'num_threads']), key=lambda p: p.info['cpu_percent'], reverse=True)][:5]
    return data

@data('top5mem')
@cache(10)
def top5_mem():
    data = [(p.pid, p.info['name'], round(p.info.get('memory_percent') or 0.0, 2), human_readable_size(p.info.get('memory_info') and p.info['memory_info'].rss, 1024, 0)) for p in sorted(psutil.process_iter(attrs=['name', 'memory_percent', 'memory_info']), key=lambda p: p.info.get('memory_percent'), reverse=True)][:5]
    return data