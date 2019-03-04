#!/usr/bin/python3
import os
import time
import argparse
import platform


def run(args):
    seconds = args.seconds
    if seconds == 0:
        clear()
        print('Input delay time in seconds:')
        seconds = int(input())
    while True:
        clear()
        if seconds == 0:
            print('Done!')
            poweroff()
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


def clear():
    command = {'Linux': 'clear', 'Windows': 'cls'}

    os.system(command[platform.system()])


def poweroff():
    command = {'Linux': 'poweroff', 'Windows': 'shutdown /s'}
    os.system(command[platform.system()])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds', '-s', default=0, type=int, required=False,
                        help='Amount of delay in seconds', dest='seconds')
    return parser.parse_args()


if __name__ == '__main__':
    try:
        run(parse_args())
    except KeyboardInterrupt:
        print()
