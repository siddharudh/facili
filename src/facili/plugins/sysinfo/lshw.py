import json
from facili import human_readable_freq, human_readable_size, human_readable_speed

def cpu_info():
    cpus = []
    find_all(get_lshw_info(), cpus, descr='CPU')
    return {
        'vendor': cpus[0]['vendor'],
        'model': cpus[0]['product'],
        'processors': len(cpus),
        'cores': sum([int(c['configuration']['cores']) for c in cpus]),
        'logical_cores': sum([int(c['configuration']['threads']) for c in cpus]),
        'speed': human_readable_freq(cpus[0]['size'])
    }
    

def mem_info():
    mem = find_first(get_lshw_info(), descr='System Memory')
    speed = filter(lambda x: x.get('clock'), mem['children'])[0]['clock']
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
        'speed': human_readable_freq(speed),
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
                'size': human_readable_size(vol['size']),
                'filesystem': vol['configuration'].get('filesystem', '')
            })
        info.append({
            'device': disk['logicalname'],
            'size': human_readable_size(disk['size']),
            'volumes': volumes
        })
    return info


def net_info():
    nets = []
    find_all(get_lshw_info(), nets, class_='network')
    info = []
    for net in nets:
        info.append({
            'vendor': net['vendor'],
            'model': net['product'],
            'speed': human_readable_speed(net['capacity'])
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

