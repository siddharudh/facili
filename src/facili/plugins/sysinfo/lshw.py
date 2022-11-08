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


import json
from facili import human_readable_freq, human_readable_size, human_readable_speed
import psutil

def cpu_info():
    cpus = []
    find_all(get_lshw_info(), cpus, descr='CPU')
    return {
        'vendor': cpus[0]['vendor'],
        'model': cpus[0]['product'],
        'processors': len(cpus),
        'cores': sum([int(c['configuration']['cores']) for c in cpus]),
        'threads': sum([int(c['configuration']['threads']) for c in cpus]),
        'speed': human_readable_freq(cpus[0]['size'])
    }
    

def mem_info():
    mem = find_first(get_lshw_info(), descr='System Memory')
    speed = ''
    valid_children = filter(lambda x: x.get('clock'), mem['children'])
    if valid_children:
        speed = valid_children[0]['clock']
    type = 'Unknown'
    if speed > 2100000000:
        type = 'DDR4'
    elif speed > 400000000:
        type = 'DDR3'
    elif speed > 200000000:
        type = 'DDR2'
    elif speed > 133000000:
        type = 'DDR1'
    return {
        'size': human_readable_size(mem['size']),
        'speed': human_readable_freq(speed) if speed else '',
        'type': type
    }


def disk_info():
    disks = []
    find_all(get_lshw_info(), disks, class_='disk')
    info = []
    for disk in disks:
        volumes = []
        for vol in disk['children']:
            volumes.append({
                'device': vol['logicalname'][0] if type(vol['logicalname']) == list else vol['logicalname'],
                'mountpoint': vol['logicalname'][1] if type(vol['logicalname']) == list else '',
                'size': human_readable_size(vol.get('size') or 0, 1),
                'filesystem': vol.get('configuration', {}).get('filesystem', '')
            })
        info.append({
            'device': disk['logicalname'],
            'size': human_readable_size(disk['size'], 1),
            'volumes': volumes
        })
    return info


def net_info():
    nets = []
    find_all(get_lshw_info(), nets, class_='network')
    info = []
    addrs = psutil.net_if_addrs()
    for net in nets:
        device = net['logicalname']
        address = netmask = ''
        if device in addrs:
            for a in addrs[device]:
                if a.family == 2:
                    address = a.address
                    netmask = sum([bin(int(x)).count("1") for x in a.netmask.split(".")])

        info.append({
            'device': device,
            'vendor': net.get('vendor') or '',
            'model': net.get('product') or '',
            'speed': human_readable_speed(net.get('capacity') or 0),
            'address': address,
            'netmask': netmask
        })
    return info

lshw_info = None

def get_lshw_info():
    global lshw_info
    if not lshw_info:
        with open('../data/lshw.json') as f:
            lshw_info = json.load(f)
    return lshw_info


def find_first(obj, class_=None, descr=None):
    if class_ and obj.get('class') == class_ or descr and obj.get('description') == descr:
        return obj
    for child in obj.get('children', []):
        match = find_first(child, class_, descr)
        if match:
            return match
    return None


def find_all(obj, result, class_=None, descr=None):
    if class_ and obj.get('class') == class_ or descr and obj.get('description') == descr:
        result.append(obj)
        return True
    for child in obj.get('children', []):
        find_all(child, result, class_, descr)
    return False

