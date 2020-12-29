#!/usr/bin/env python3
# -*- coding: future_fstrings -*-

import argparse, sys, os
from collections import defaultdict
from db_sync_tool.utility import helper
# Workaround for ModuleNotFoundError
sys.path.append(os.getcwd())
from file_sync_tool import sync


def main(args={}):
    """
    Main entry point for the command line. Parse the arguments and call to the main process.
    :param args:
    :return:
    """
    args = get_arguments(args)
    config = build_config(args)
    sync.Sync(
        config_file=args.config_file,
        verbose=args.verbose,
        mute=args.mute,
        host_file=args.host_file,
        config=config
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


def build_config(args):
    """
    Building an optional config
    :param args:
    :return:
    """
    config = defaultdict(dict)
    config['target'] = defaultdict(dict)
    config['origin'] = defaultdict(dict)

    if not args.target_host is None:
        config['target']['host'] = args.target_host

    if not args.target_user is None:
        config['target']['user'] = args.target_user

    if not args.target_password is None:
        config['target']['password'] = args.target_password

    if not args.target_key is None:
        config['target']['ssh_key'] = args.target_key

    if not args.target_port is None:
        config['target']['port'] = args.target_port

    if not args.origin_host is None:
        config['origin']['host'] = args.origin_host

    if not args.origin_user is None:
        config['origin']['user'] = args.origin_user

    if not args.origin_password is None:
        config['origin']['password'] = args.origin_password

    if not args.origin_key is None:
        config['origin']['ssh_key'] = args.origin_key

    if not args.origin_port is None:
        config['origin']['port'] = args.origin_port

    if not args.files_origin is None:
        if 'config' not in config['files']:
            config['files']['config'] = []
            config['files']['config'].append({})
        config['files']['config'][0]['origin'] = args.files_origin

    if not args.files_target is None:
        if 'config' not in config['files']:
            config['files']['config'] = []
            config['files']['config'].append({})
        config['files']['config'][0]['target'] = args.files_target

    if not args.files_exclude is None:
        config['files']['config'][0]['exclude'] = args.files_exclude.split(',')

    if not args.files_option is None:
        config['files']['option'] = args.files_option.split(',')

    return config


if __name__ == "__main__":
    main()
