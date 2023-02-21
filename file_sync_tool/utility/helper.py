#!/usr/bin/env python3
# -*- coding: future_fstrings -*-

import sys
import os
import re
from db_sync_tool.utility import mode, system, output
from file_sync_tool.transfer import utility


def check_rsync_version():
    """
    Check rsync version
    :return:
    """
    _raw_version = mode.run_command(
        'rsync --version',
        mode.Client.LOCAL,
        True
    )
    _version = parse_version(_raw_version)
    output.message(
        output.Subject.LOCAL,
        f'rsync version {_version}'
    )


def check_sshpass_version():
    """
    Check sshpass version
    :return:
    """
    system.config['use_sshpass'] = False
    _raw_version = mode.run_command(
        'sshpass -V',
        mode.Client.LOCAL,
        force_output=True,
        allow_fail=True
    )
    _version = parse_version(_raw_version)

    if _version:
        output.message(
            output.Subject.LOCAL,
            f'sshpass version {_version}'
        )
        system.config['use_sshpass'] = True
        return True


def parse_version(output):
    """
    Parse version out of console output
    https://stackoverflow.com/a/60730346
    :param output: String
    :return:
    """
    _version_pattern = r'\d+(=?\.(\d+(=?\.(\d+)*)*)*)*'
    _regex_matcher = re.compile(_version_pattern)
    _version = _regex_matcher.search(output)
    if _version:
        return _version.group(0)
    else:
        return None


def check_authorizations():
    """
    Check authorization for clients
    :return:
    """
    if system.config['use_sshpass']:
        # When using sshpass, check for passwords
        system.check_authorization(mode.Client.ORIGIN)
        system.check_authorization(mode.Client.TARGET)
    elif not 'ssh_key' in system.config[mode.Client.ORIGIN] and \
            not 'ssh_key' in system.config[mode.Client.TARGET] and \
            (mode.get_sync_mode() == mode.SyncMode.PROXY or len(system.config['files']['config']) > 1):
        # Suggest to install sshpass
        output.message(
            output.Subject.INFO,
            f'Suggestion: Install {output.CliFormat.BOLD}sshpass{output.CliFormat.ENDC} to avoid multiple input of ssh passwords'
        )


def dict_to_args(dict):
    """
    Convert an dictionary to a args list
    :param dict: Dictionary
    :return: List
    """
    _args = []
    for key, val in dict.items():
        if isinstance(val, bool):
            if val:
                _args.append(f'--{key}')
        else:
            _args.append(f'--{key}')
            _args.append(str(val))
    if len(_args) == 0:
        return None
    return _args


def adjust_sync_mode():
    """

    :return:
    """
    if mode.get_sync_mode() == mode.SyncMode.DUMP_LOCAL:
        mode.sync_mode = mode.SyncMode.SYNC_LOCAL
    if mode.get_sync_mode() == mode.SyncMode.DUMP_REMOTE:
        mode.sync_mode = mode.SyncMode.SYNC_REMOTE


def extend_config(args):
    """
    Extending optional config
    :param args:
    :return:
    """
    config = system.config

    if args is None or not args:
        return config

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
