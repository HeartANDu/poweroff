#!/usr/bin/python3
import os
import time
import argparse
import platform


SYSTEM_UTIL_NAMES = {'Linux': {'poweroff': 'poweroff',
                               'clear': 'clear'},
                     'Windows': {'poweroff': 'shutdown /s',
                                 'clear': 'cls'}}


def run():
    commands = SYSTEM_UTIL_NAMES[platform.system()]
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds', '-s', default=0, type=int, required=False,
                        help='Amount of delay in seconds', dest='seconds')
    args = parser.parse_args()
    seconds = args.seconds
    if seconds == 0:
        os.system(commands['clear'])
        print('Input delay time in seconds:')
        seconds = int(input())
    while True:
        os.system(commands['clear'])
        if seconds == 0:
            print('Done!')
            os.system(commands['poweroff'])
            break
        print('Time remaining: ' + format_time(seconds))
        time.sleep(1)
        seconds -= 1


def format_time(seconds: int) -> str:
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        pass
