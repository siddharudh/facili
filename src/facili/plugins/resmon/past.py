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


class samples_store:
    def __init__(self, fields):
        self.fields = fields
        self.reset_samples()

    def reset_samples(self):
        self.samples = {f: list() for f in self.fields}

    def add_sample(self, sample):
        for f in self.fields:
            self.samples[f].append(sample.get(f) or 0)

    def get_max_values(self):
        max_values = {}
        for f in self.fields:
            if self.samples[f]:
                max_values[f] = max(self.samples[f])
        return max_values


def samples_loader(res_type, date):
    if not res_type or not date:
        return
    path = os.path.join(*(DATA_DIR + [res_type, date + '.log']))
    if os.path.exists(path):
        with open(path) as log_file:
            for line in log_file:
                sample = json.loads(line)
                yield sample


def build_samples_output(res_type, fields, level=1):
    result = {}
    q = get_query()
    result.update(q)
    interval = 0
    try:
        interval = int(q.get('i'))
    except:
        pass
    next_t = 0
    samples = []
    ss_map = {'': samples_store(fields)}
    for sample in samples_loader(res_type, q.get('d')):
        if level == 1:
            ss_map[''].add_sample(sample)
        elif level == 2:
            for k in sample:
                if type(sample[k]) == dict:
                    if k not in ss_map:
                        ss_map[k] = samples_store(fields)
                    ss_map[k].add_sample(sample[k])
        if sample['t'] >= next_t:
            data = {}
            if level == 1:
                data = ss_map[''].get_max_values()
                ss_map[''].reset_samples()
            else:
                for k in ss_map:
                    if k:
                        data[k] = ss_map[k].get_max_values()
                        ss_map[k].reset_samples()
            if data:
                data['t'] = sample['t']
                samples.append(data)
            next_t = sample['t'] + interval
    result['samples'] = samples
    return result


@data('_cpu')
def past_cpu_data():
    return build_samples_output('cpu', ['ac', 'l'])

@data('_mem')
def past_mem_data():
    return build_samples_output('mem', ['p'])


@data('_disk')
def past_disk_data():
    return build_samples_output('disk', ['p'], 2)


@data('_disk_io')
def past_disk_io_data():
    return build_samples_output('disk_io', ['r', 'w'], 2)


@data('_net_io')
def past_net_io_data():
    return build_samples_output('net_io', ['r', 's'], 2)
