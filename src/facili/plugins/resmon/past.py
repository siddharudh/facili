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


from facili import data, get_query
import os
import json


DATA_DIR = ['..', 'data', 'plugins', 'resmon']


def build_samples_output(res_type, *keys):
    result = {}
    q = get_query()
    result.update(q)
    t, d, i = q.get('t'), q.get('d'), q.get('i')
    interval = 0
    try:
        interval = int(i)
    except:
        pass
    next_t = 0
    temp = {k: list() for k in keys}
    if d:
        path = os.path.join(*(DATA_DIR + [res_type, d + '.log']))
        if os.path.exists(path):
            samples = []
            with open(path) as log_file:
                for line in log_file:
                    sample = json.loads(line)
                    for k in keys:
                        temp[k].append(sample.get(k) or 0)
                    if sample['t'] >= next_t:
                        data = {}
                        for k in keys:
                            if temp[k]:
                                data[k] = max(temp[k])
                        if data:
                            data['t'] = sample['t']
                            samples.append(data)
                        temp = {k: list() for k in keys}
                        next_t = sample['t'] + interval
            result['samples'] = samples
    return result


@data('_cpu')
def past_cpu_data():
    return build_samples_output('cpu', 'ac', 'l')

@data('_mem')
def past_cpu_data():
    return build_samples_output('mem', 'p')
