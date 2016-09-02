#!/usr/bin/env python3
import sys
import os
from functools import partial
from subprocess import check_output, CalledProcessError

from selector.selector import select_from_list

if __name__ == '__main__':
    try:
        lines = check_output(['git', 'grep', '-n'] + sys.argv[1:]).splitlines()
    except CalledProcessError as e:
        sys.exit(1)
    else:
        lines = tuple(map(partial(bytes.decode, encoding='utf-8'), lines))
        selection = select_from_list(lines)
        path, line_number, match = selection.selected.split(':', maxsplit=2)
        args = os.environ.get('EDITOR', 'vim').split()
        args.append('+{}'.format(line_number))
        args.append(path)
        args.append(os.environ)
        os.execlpe(args[0], *args)
