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


'''
Logs

System log files viewer
'''

from facili import data, cache
import os
import psutil

LINES_COUNT = 1000


def shell_command_output(cmd):
    with os.popen(cmd) as p:
        return p.read()


SYSLOGS = []
if psutil.LINUX:
    SYSLOGS = ['/var/log/syslog.2', '/var/log/syslog.1', '/var/log/syslog']
elif psutil.MACOS:
    SYSLOGS = ['/var/log/system.log']

@data('_syslog')
@cache(5)
def get_syslog():
    syslogs = filter(lambda p: os.path.exists(p), SYSLOGS)
    if syslogs:
        return shell_command_output('cat %s | tail -n%d' % (' '.join(syslogs), LINES_COUNT))

KERNLOGS = ['/var/log/kern.log.1', '/var/log/kern.log']

@data('_kernlog')
@cache(5)
def get_kernlog():
    if psutil.LINUX:
        kernlogs = filter(lambda p: os.path.exists(p), KERNLOGS)
        if kernlogs:
            return shell_command_output('cat %s | tail -n%d' % (' '.join(kernlogs), LINES_COUNT))
    elif psutil.MACOS:
        return shell_command_output('dmesg | tail -n%d' % LINES_COUNT)
