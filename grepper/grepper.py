#!/usr/bin/env python3
import sys
from subprocess import check_call

if __name__ == '__main__':
    check_call(['git', 'grep'] + sys.argv[1:])
