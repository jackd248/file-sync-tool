#!/usr/bin/env python3
# -*- coding: future_fstrings -*-

import re
import datetime
import os
import shutil
from db_sync_tool.utility import system, mode, output
from file_sync_tool.utility import helper

# Default options for rsync command
# https://wiki.ubuntuusers.de/rsync/
default_options = [
    '--delete',
    '-a',
    '-z',
    '--stats',
    '--human-readable',
    '--iconv=UTF-8',
    '--chmod=D2770,F660'
]

# Temporary data directory (for PROXY mode)
temp_data_dir = None


def get_password_environment(client):
    """
    Optionally create a password environment variable for sshpass password authentication
    https://www.redhat.com/sysadmin/ssh-automation-sshpass
    :param client: String
    :return:
    """
    if not client:
        return ''

    if system.config['use_sshpass'] and not 'ssh_key' in system.config[client] and 'password' in system.config[client]:
        return f'SSHPASS=\'{system.config[client]["password"]}\' '
    return ''


def get_authorization(client):
    """
    Define authorization arguments for rsync command
    :param client: String
    :return: String
    """
    _ssh_key = None
    if not client:
        return ''

    if 'ssh_key' in system.config[client]:
        _ssh_key = system.config[mode.Client.ORIGIN]['ssh_key']

    _ssh_port = system.config[client]['port'] if 'port' in system.config[client] else 22

    if _ssh_key is None:
        if system.config['use_sshpass'] and get_password_environment(client):
            # In combination with SSHPASS environment variable
            # https://www.redhat.com/sysadmin/ssh-automation-sshpass
            return f'--rsh="sshpass -e ssh -p{_ssh_port} -o StrictHostKeyChecking=no -l {system.config[client]["user"]}"'
        else:
            return f'-e "ssh -p{_ssh_port} -o StrictHostKeyChecking=no"'
    else:
        # Provide ssh key file path for ssh authentication
        return f'-e "ssh -i {_ssh_key} -p{_ssh_port}"'


def get_host(client):
    """
    Return user@host if client is not local
    :param client: String
    :return: String
    """
    if mode.is_remote(client):
        return f'{system.config[client]["user"]}@{system.config[client]["host"]}:'
    return ''


def get_options():
    """
    Prepare rsync options with stored default options and provided addtional options
    :return: String
    """
    _options = f'{" ".join(default_options)}'
    if 'option' in system.config['files']:
        _options += f'{" ".join(system.config["files"]["option"])}'
    return _options


def get_excludes(excludes):
    """
    Prepare rsync excludes as arguments
    :param excludes:
    :return:
    """
    _excludes = ''
    for exclude in excludes:
        _excludes += f'--exclude {exclude} '
    return _excludes


def read_stats(stats):
    """
    Read rsync stats and print a summary
    :param stats: String
    :return:
    """
    if system.config['verbose']:
        print(f'{output.Subject.DEBUG}{output.CliFormat.BLACK}{stats}{output.CliFormat.ENDC}')

    _file_number = parse_string(stats, r'Number of regular files transferred:\s*([\d.]+)')
    _file_size = parse_string(stats, r'Total transferred file size:\s*([\d.]+[MKG]?)')

    if _file_number and _file_size:
        output.message(
            output.Subject.INFO,
            f'Status: {_file_number[0]} file(s) transferred {output.CliFormat.BLACK}({_file_size[0]}Bytes){output.CliFormat.ENDC}'
        )


def parse_string(string, regex):
    """
    Parse string by given regex
    :param string: String
    :param regex: String
    :return:
    """
    _file_size_pattern = regex
    _regex_matcher = re.compile(_file_size_pattern)
    return _regex_matcher.findall(string)


def generate_temp_dir_name():
    """
    Generate a temporary directory name, e.g. _tmp_28-12-2020_15-59
    :return:
    """
    global temp_data_dir
    _now = datetime.datetime.now()
    temp_data_dir = f'/tmp/_tmp_{_now.strftime("%d-%m-%Y_%H-%M")}'


def remove_temporary_dir():
    """
    Remove temporary directory
    :return:
    """
    global temp_data_dir
    if os.path.exists(temp_data_dir):
        shutil.rmtree(temp_data_dir)
        output.message(
            output.Subject.LOCAL,
            'Cleaning up',
            True
        )
