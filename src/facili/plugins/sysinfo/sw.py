from facili import data, cache
import subprocess
import re

SW_VER_ENTRIES = (
    ('kernel', 'uname -r', r'(.+)'),
    ('lsb', 'lsb_release -d', r'Description:\s*(.+)'),

    # languages
    ('python', 'python -V', r'Python\s*(.+)'),
    ('java', 'java -version', r'java version "(.+)"'),

    # databases
    ('mongodb', 'mongod --version', r'db version v(.+)'),
    ('mysql', 'mysqld --version', r'mysqld\s+Ver\s+([0-9\.]+)'),
    ('postgres', 'postgres -V', r'([0-9\.]+)'),

    # web servers
    ('nginx', 'nginx -v', r'nginx version: nginx/(.+)'),

    # ftp, smb servers
    ('proftpd', 'proftpd -v', r'ProFTPD Version (.+)'),
    ('smbd', 'smbd -V', r'Version (.+)'),

    # utilities
    ('ffmpeg', 'ffmpeg -version', r'ffmpeg version ([0-9\.]+)'),
)


def program_output(cmd):
    try:
        return subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT)
    except:
        pass
    return ''

def extract(pattern, data):
    try:
        return re.search(pattern, data, re.I).group(1)
    except:
        pass
    return ''


def get_sw_versions():
    sw_versions = []
    for program, command, pattern in SW_VER_ENTRIES:
        version = extract(pattern, program_output(command))
        if version:
            sw_versions.append([program, version])
    return sw_versions


@data('ver')
@cache(3600)
def sw_version_info():
    return get_sw_versions()