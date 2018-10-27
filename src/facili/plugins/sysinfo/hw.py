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
