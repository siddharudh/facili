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


from facili import data, cache
from collections import OrderedDict
import psutil
import os


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


@data('disk_io')
@cache(5)
def disk_io_usage():
    usage = OrderedDict()
    dio = psutil.disk_io_counters(True)
    for d in dio:
        usage[d] = vars(dio[d])
    return usage


@data('net_io')
@cache(5)
def net_io_usage():
    usage = OrderedDict()
    nio = psutil.net_io_counters(True)
    for n in nio:
        usage[n] = vars(nio[n])
    return usage