from facili import data
import psutil
import socket
import datetime

@data('mount')
def mount_data():
    mount_points = []
    for dp in psutil.disk_partitions(True):
        mount_points.append(vars(dp))
    return mount_points

@data('')
def misc_data():
    return {
        'hostname': socket.gethostname(),
        'boot_time': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    }