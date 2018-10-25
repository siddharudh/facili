
def human_readable(val, suffixes, base):
    for i, suffix in enumerate(suffixes):
        if val >= base ** (len(suffixes) - i - 1):
            return '%0.2f %s' % (float(val) / base ** (len(suffixes) - i - 1), suffix)


def human_readable_size(size, base=1024):
    if base == 1024:
        return human_readable(size, ['TiB', 'GiB', 'MiB', 'KiB', 'Bytes'], 1024)
    elif base == 1000:
        return human_readable(size, ['TB', 'GB', 'MB', 'KB', 'Bytes'], 1000)


def human_readable_freq(freq):
    return human_readable(freq, ['GHz', 'MHz', 'KHz', 'Hz'], 1000)


def human_readable_speed(speed):
    return human_readable(speed, ['Gbps', 'Mbps', 'Kbps', 'bit/s'], 1000)

