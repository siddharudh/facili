from facili import get_data, timer
import json
import time


@timer(1)
def capture_data():
    """
    1) Collect samples every second
    Split data files day-wise: 60 * 60 * 24 = 86400 entries per file
    Keep past 7 days data

    2) Collect samples every 5 seconds
    Split data files day-wise: 12 * 60 * 24 = 17280 entries per file
    Keep past 365 days data
    """
    data = get_data('resmon.live')
    with open('facili.data', 'a') as f:
        data['time'] = int(time.time())
        json.dump(data, f)
        f.write('\r\n')
