#!/usr/bin/python

import sys, os
import getopt
from peanuts import load as load_peanuts
from elvis.climanager import clean, create_peanut as manager_create_peanut

ARG_OPTIONS = (
    'hlLr:c:V',
    ['help', 'list', 'list-all', 'run=', 'create=', 'verbose']
)

def usage(willExit=True):
    f = open('./logo')
    print(f.read())
    f.close()
    print("""Usage:
    python elvis.py [options]

General Options:
    -h, --help                          Display help
    -l, --list                          Display list of available peanuts
    -L, --list-all                      Display complete list of peanuts
    -r, --run peanut1,peanut2,...       Run selected peanuts in the order given
    -c, --create peanut_name            Create a peanut, name must not have spaces
    -V, --verbose                       Verbose mode

Source:
    https://github.com/donkeysharp/elvispy
""")
    if willExit:
        exit(0)


AVAILABLE_PEANUTS = {}
def list_peanuts(verbose=False):
    print('List of available peanuts:')
    for name in AVAILABLE_PEANUTS.keys():
        peanut = AVAILABLE_PEANUTS[name]
        if not verbose:
            print('     [*] %s' % name)
        else:
            print('     [*] %s - %s' % (name, peanut.info['description']))


def run_peanuts(peanut_list):
    print('Running peanuts...')
    for peanut in peanut_list:
        if not AVAILABLE_PEANUTS.has_key(peanut):
            print('Peanut %s is not available or it does not exist.' % peanut)
            exit(0)
    for peanut in peanut_list:
        AVAILABLE_PEANUTS[peanut].start()


def create_peanut(peanut_name):
    manager_create_peanut(peanut_name)


def main(args):
    global AVAILABLE_PEANUTS
    try:
        opts, args = getopt.getopt(args, ARG_OPTIONS[0], ARG_OPTIONS[1])
    except getopt.GetoptError:
        usage()

    list_flag = list_all_flag = run_flag = help_flag = False
    create_flag = verbose_flag = False
    peanut_list = []
    new_peanut_name = ''
    for opt, value in opts:
        if opt in ('-l', '--list'):
            list_flag = True
        if opt in ('-L', '--list-all'):
            list_all_flag = True
        elif opt in ('-h', '--help'):
            help_flag = True
        elif opt in ('-r', '--run'):
            run_flag = True
            peanut_list = value.split(',')
        elif opt in ('-c', '--create'):
            create_flag = True
            new_peanut_name = value
        elif opt in ('-V', '--verbose'):
            verbose_flag = True

    AVAILABLE_PEANUTS = load_peanuts(list_all_flag)

    if help_flag:
        usage()
    elif list_flag or list_all_flag:
        list_peanuts(verbose_flag)
    elif run_flag:
        run_peanuts(peanut_list)
    elif create_flag:
        create_peanut(new_peanut_name)
    else:
        usage()

    clean()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        usage()
    main(sys.argv[1:])
