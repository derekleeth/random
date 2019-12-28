#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""copy-files.py

Copy files to external storage.
"""

import sys
import os
import subprocess
import argparse


def Main(source, destination, excludedirsfilepath, logpath):
    '''
    robocopy $Source $Destination /MAXAGE:30 /R:30 /W:10 /dcopy:DAT /Z /S /log:$RoboCopyLog
    '''
    if not logpath:
        logFile = "{log}{uri}.txt".format(log = logs, uri = targetUri)

    cmd = [
            'Robocopy.exe',
            os.path.abspath(source),
            os.path.abspath(destination)
        ]
    
    copyProcess = subprocess.Popen(cmd)


def _cli():
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)
    parser.add_argument('-s', '--source', help="This is the foo argument")
    parser.add_argument('-d', '--destination', help="This is the bar argument")
    parser.add_argument('-ed', '--excludedirsfilepath', default="", help="This is the bar argument")
    parser.add_argument('-l', '--logpath', default="", help="This is the bar argument")
    qux_help = ("This argument will show its default in the help due to "
                "ArgumentDefaultsHelpFormatter")
    # parser.add_argument('-q', '--qux', default=3, help=qux_help)
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    main(**_cli())