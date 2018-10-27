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
from collections import OrderedDict
from facili import human_readable_size

def cpu_info():
    dmi_info = get_dmi_info()
    proc = dmi_info['Processor Information']
    return {
        'vendor': proc[0]['Manufacturer'],
        'model': proc[0]['Version'],
        'processors': len(proc),
        'cores': sum([int(p['Core Count']) for p in proc]),
        'threads': sum([int(p['Thread Count']) for p in proc]),
        'speed': proc[0]['Current Speed']
    }

def mem_info():
    dmi_info = get_dmi_info()
    mem = dmi_info['Memory Device']
    total_size = 0
    mem_type = None
    mem_speed = 0
    for m in mem:
        if m['Type'] != 'Unknown':
            mem_type = m['Type']
            try:
                total_size += int(filter(str.isdigit, m['Size'])) * 1024 * 1024
            except:
                pass
            mem_speed = m['Speed']

    return {
        'size': human_readable_size(total_size),
        'type': mem_type,
        'speed': mem_speed
    }

dmi_info = None

def get_dmi_info():
    global dmi_info
    if not dmi_info:
        with open('../data/dmidecode.txt') as f:
            dmi_info = parse_dmidecode_output(f.read())
    return dmi_info

def indent_level(line):
    l = 0
    for c in line:
        if c != '\t':
            break
        l += 1
    return l

def key_value(line):
    kv = line.split(':', 1)
    if len(kv) == 2 and kv[1].strip() != '':
        return kv[0].strip(), kv[1].strip()
    return None, None

def parse_dmidecode_output(data):
    dmi_info = OrderedDict()
    section = OrderedDict()
    start = False
    for line in data.split('\n'):
        if line.startswith('Handle'):
            start = True
        if not line or not start:
            continue
        indent = indent_level(line)
        line = line.strip()
        if indent == 0 and not line.startswith('Handle '):
            section_name = line
            sections = dmi_info.get(section_name, [])
            dmi_info[section_name] = sections
            section = OrderedDict()
            sections.append(section)
            multival = None
        elif indent == 1:
            if line.endswith(':'):
                multival_key = line.rstrip(':')
                section[multival_key] = multival = []
            else:
                key, val = key_value(line)
                if key:
                    section[key] = val
                multival = None
        elif indent == 2 and multival != None:
            multival.append(line)
    return dmi_info


