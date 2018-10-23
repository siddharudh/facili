from facili import data
from collections import OrderedDict
import psutil


@data('cpu')
def cpu_usage():
    per_cpu_percent = psutil.cpu_percent(0.1, True)
    return {
        'per_cpu': per_cpu_percent,
        'avg': round(sum(per_cpu_percent) / len(per_cpu_percent), 2)
    }


@data('mem')
def mem_usage():
    return vars(psutil.virtual_memory())


@data('swap')
def swap_usage():
    return vars(psutil.swap_memory())


@data('disk')
def disk_usage():
    usage = OrderedDict()
    for dp in psutil.disk_partitions():
        du = psutil.disk_usage(dp.mountpoint)
        usage[dp.mountpoint] = vars(du)
    return usage


@data('disk_io')
def disk_io_usage():
    usage = OrderedDict()
    dio = psutil.disk_io_counters(True)
    for d in dio:
        usage[d] = vars(dio[d])
    return usage


@data('net_io')
def net_io_usage():
    usage = OrderedDict()
    nio = psutil.net_io_counters(True)
    for n in nio:
        usage[n] = vars(nio[n])
    return usage