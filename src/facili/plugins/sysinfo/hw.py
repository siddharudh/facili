
from facili import data, cache
import lshw
import dmi


@data('cpu')
@cache()
def cpu_info():
    return lshw.cpu_info()


@data('mem')
@cache()
def mem_info():
    return lshw.mem_info()


@data('disk')
@cache()
def disk_info():
    return lshw.disk_info()


@data('net')
@cache()
def net_info():
    return lshw.net_info()


@data('_lshw')
@cache()
def _lshw_info():
    return lshw.get_lshw_info()


@data('_dmi')
@cache()
def _dmi_info():
    return dmi.get_dmi_info()
