from facili import data, cache
import psutil
import socket
import datetime

@data('mount')
@cache(60)
def mount_data():
    mount_points = []
    for dp in psutil.disk_partitions(True):
        mount_points.append(vars(dp))
    return mount_points

@data('')
@cache(60)
def misc_data():
    return {
        'hostname': socket.gethostname(),
        'boot_time': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    }