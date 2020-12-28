#!/usr/bin/env python3
# -*- coding: future_fstrings -*-

import argparse, sys, os
from collections import defaultdict
# Workaround for ModuleNotFoundError
sys.path.append(os.getcwd())
from db_sync_tool.utility import helper
from file_sync_tool import sync


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
        config={}
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

    return parser.parse_args(helper.dict_to_args(args))


if __name__ == "__main__":
    main()
