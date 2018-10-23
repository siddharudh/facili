
from facili import data
import random

@data('cpu')
def cpu_info():
    return {
        'vendor': 'GenuineIntel',
        'model': 'Xeon E7 v2',
        'processors': 1,
        'cores': 6,
        'logical_cores': 12,
        'speed': '1.8 GHz',
        'rand': random.randint(1, 100)
    }


@data('mem')
def mem_info():
    return {
        "size": "16 GB",
        "type": "DDR3",
        "speed": "1600 MHz"
    }


@data('raid')
def raid_info():
    return {
    }


@data('disk')
def disk_info():
    return {
    }

