
from facili import data
import lshw
import dmi


@data('cpu')
def cpu_info():
    return lshw.cpu_info()


@data('mem')
def mem_info():
    return lshw.mem_info()


@data('disk')
def disk_info():
    return lshw.disk_info()


@data('net')
def net_info():
    return lshw.net_info()


@data('_lshw')
def _lshw_info():
    return lshw.get_lshw_info()


@data('_dmi')
def _dmi_info():
    return dmi.get_dmi_info()
