#!/usr/bin/env python3
# -*- coding: future_fstrings -*-

import argparse, sys, os
from collections import defaultdict
# Workaround for ModuleNotFoundError
sys.path.append(os.getcwd())
from file_sync_tool import sync
from file_sync_tool.utility import helper


def main(args={}):
    """
    Main entry point for the command line. Parse the arguments and call to the main process.
    :param args:
    :return:
    """
    args = get_arguments(args)
    sync.Sync(
        config_file=args.config_file,
        verbose=args.verbose,
        mute=args.mute,
        host_file=args.host_file,
        args=args
    )


def get_arguments(args):
    """
    Parses and returns script arguments
    :param args:
    :return:
    """
    parser = argparse.ArgumentParser(prog='file_sync_tool', description='A tool for automatic file synchronization from and to host systems.')
    parser.add_argument('-f', '--config-file',
                        help='Path to configuration file',
                        required=False,
                        type=str)
    parser.add_argument('-v', '--verbose',
                        help='Enable extended console output',
                        required=False,
                        action='store_true')
    parser.add_argument('-m', '--mute',
                        help='Mute console output',
                        required=False,
                        action='store_true')
    parser.add_argument('-o', '--host-file',
                        help='Using an additional hosts file for merging hosts information with the configuration file',
                        required=False,
                        type=str)
    parser.add_argument('-th', '--target-host',
                        help='SSH host to target system',
                        required=False,
                        type=str)
    parser.add_argument('-tu', '--target-user',
                        help='SSH user for target system',
                        required=False,
                        type=str)
    parser.add_argument('-tpw', '--target-password',
                        help='SSH password for target system',
                        required=False,
                        type=str)
    parser.add_argument('-tk', '--target-key',
                        help='File path to SSH key for target system',
                        required=False,
                        type=str)
    parser.add_argument('-tpo', '--target-port',
                        help='SSH port for target system',
                        required=False,
                        type=int)
    parser.add_argument('-oh', '--origin-host',
                        help='SSH host to origin system',
                        required=False,
                        type=str)
    parser.add_argument('-ou', '--origin-user',
                        help='SSH user for origin system',
                        required=False,
                        type=str)
    parser.add_argument('-opw', '--origin-password',
                        help='SSH password for origin system',
                        required=False,
                        type=str)
    parser.add_argument('-ok', '--origin-key',
                        help='File path to SSH key for origin system',
                        required=False,
                        type=str)
    parser.add_argument('-opo', '--origin-port',
                        help='SSH port for origin system',
                        required=False,
                        type=int)
    parser.add_argument('-fo', '--files-origin',
                        help='File path for origin source of file sync',
                        required=False,
                        type=str)
    parser.add_argument('-ft', '--files-target',
                        help='File path for target destination of file sync',
                        required=False,
                        type=str)
    parser.add_argument('-fe', '--files-exclude',
                        help='Excludes for file sync',
                        required=False,
                        type=str)
    parser.add_argument('-fop', '--files-option',
                        help='Additional rsync options',
                        required=False,
                        type=str)

    return parser.parse_args(helper.dict_to_args(args))


if __name__ == "__main__":
    main()
