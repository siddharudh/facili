from facili import data
import psutil

@data('mount')
def mount_data():
    mount_points = []
    for dp in psutil.disk_partitions(True):
        mount_points.append(vars(dp))
    return mount_points
