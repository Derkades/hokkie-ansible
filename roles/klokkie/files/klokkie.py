#!/usr/bin/env python3
import time
from termcolor import colored
from pyfiglet import figlet_format

REMOVE_CURSOR = "\x1b[?25l"
CLEAR = "\33[H\33[2J\33[3J"

print(REMOVE_CURSOR)

while True:
    clock = colored(figlet_format(time.strftime("%H:%M:%S", time.localtime()), font='big'), 'white', attrs=['bold'])
    print(CLEAR + clock)
    time.sleep(1)
