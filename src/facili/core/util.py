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


def human_readable(val, suffixes, base, decimal=2):
    for i, suffix in enumerate(suffixes):
        if val >= base ** (len(suffixes) - i - 1):
            v = round(float(val) / base ** (len(suffixes) - i - 1), decimal)
            if v == int(v):
                return '%d %s' % (int(v), suffix)
            else:
                return '%0.*f %s' % (decimal, v, suffix)


def human_readable_size(size, decimal=2, base=1024):
    if base == 1024:
        return human_readable(size, ['TiB', 'GiB', 'MiB', 'KiB', 'Bytes'], 1024, decimal)
    elif base == 1000:
        return human_readable(size, ['TB', 'GB', 'MB', 'KB', 'Bytes'], 1000, decimal)


def human_readable_freq(freq, decimal=2):
    return human_readable(freq, ['GHz', 'MHz', 'KHz', 'Hz'], 1000, decimal)


def human_readable_speed(speed, decimal=2):
    return human_readable(speed, ['Gbps', 'Mbps', 'Kbps', 'bit/s'], 1000, decimal)


def human_readable_dur(total_seconds):
    hhmmss = ''
    ts = int(total_seconds)
    hours = minutes = seconds = 0
    hours = ts / 3600
    if hours > 0:
        hhmmss += '%d:' % hours
        ts %= 3600
    minutes = ts / 60
    if hhmmss:
        hhmmss += '%02d:' % minutes
        ts %= 60
    elif minutes > 0:
        hhmmss += '%d:' % minutes
        ts %= 60
    if hhmmss:
        hhmmss += '%02d' % ts
    else:
        hhmmss += '%d' % ts
    return hhmmss
