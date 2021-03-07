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


def adjust_sync_mode():
    """

    :return:
    """
    if mode.get_sync_mode() == mode.SyncMode.DUMP_LOCAL:
        mode.sync_mode = mode.SyncMode.SYNC_LOCAL
    if mode.get_sync_mode() == mode.SyncMode.DUMP_REMOTE:
        mode.sync_mode = mode.SyncMode.SYNC_REMOTE