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
