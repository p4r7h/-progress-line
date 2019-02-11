

import sys


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', status))
sys.stdout.flush()

import time 


total = 1000
i = 0
while i < total:
    progress(i, total, status='rootkit uploading...')
    time.sleep(0.2)  # emulating long-playing job
    i += 1
