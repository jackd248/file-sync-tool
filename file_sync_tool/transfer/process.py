#!/usr/bin/env python3
# -*- coding: future_fstrings -*-

from db_sync_tool.utility import mode, system, output, helper
from db_sync_tool.remote import client as remote_client
from file_sync_tool.transfer import utility


def transfer_files():
    """
    Transfering configured files between clients
    :return:
    """
    if 'files' in system.config:
        for config in system.config['files']['config']:
            output.message(
                output.Subject.INFO,
                f'Starting rsync file transfer'
            )

            if 'exclude' not in config:
                config['exclude'] = []

            if mode.get_sync_mode() == mode.SyncMode.PROXY:
                # Proxy mode: Transferring from origin to local and from local to target
                utility.generate_temp_dir_name()
                helper.check_and_create_dump_dir(mode.Client.LOCAL, utility.temp_data_dir)
                synchronize(
                    origin_path=config[mode.Client.ORIGIN],
                    target_path=utility.temp_data_dir,
                    exclude=config['exclude'],
                    pseudo_client=mode.Client.ORIGIN
                )
                synchronize(
                    origin_path=f'{utility.temp_data_dir}/*',
                    target_path=config[mode.Client.TARGET],
                    exclude=config['exclude'],
                    pseudo_client=mode.Client.TARGET
                )
                utility.remove_temporary_dir()
            elif mode.get_sync_mode() == mode.SyncMode.SYNC_REMOTE:
                synchronize(
                    origin_path=config[mode.Client.ORIGIN],
                    target_path=config[mode.Client.TARGET],
                    exclude=config['exclude'],
                    client=mode.Client.ORIGIN,
                    force_remote=True
                )
            else:
                synchronize(
                    origin_path=config[mode.Client.ORIGIN],
                    target_path=config[mode.Client.TARGET],
                    exclude=config['exclude']
                )
    else:
        f'{output.Subject.WARNING} No file sync configuration provided'


def synchronize(origin_path, target_path, exclude, client=mode.Client.LOCAL, pseudo_client=None, force_remote=False):
    """
    Using rsync command to synchronize files between systems
    :param origin_path: String
    :param target_path: String
    :param exclude: List
    :param client: String
    :param pseudo_client: String Client, which will be forced as remote client. Necessary for proxy transfer.
    :param force_remote: Boolean
    :return:
    """
    _remote_client = None
    if force_remote:
        remote_client.load_ssh_client_origin()
        _origin_subject = f'{output.Subject.ORIGIN}{output.CliFormat.BLACK}[REMOTE]{output.CliFormat.ENDC} '
        _target_subject = f'{output.Subject.TARGET}{output.CliFormat.BLACK}[REMOTE]{output.CliFormat.ENDC} '
    elif mode.is_remote(mode.Client.ORIGIN) and pseudo_client != mode.Client.TARGET:
        _remote_client = mode.Client.ORIGIN
        _origin_subject = f'{output.Subject.ORIGIN}{output.CliFormat.BLACK}[REMOTE]{output.CliFormat.ENDC} '
        _target_subject = f'{output.Subject.TARGET}{output.CliFormat.BLACK}[LOCAL]{output.CliFormat.ENDC} '
    elif mode.is_remote(mode.Client.TARGET) and pseudo_client != mode.Client.ORIGIN:
        _remote_client = mode.Client.TARGET
        _origin_subject = f'{output.Subject.ORIGIN}{output.CliFormat.BLACK}[LOCAL]{output.CliFormat.ENDC} '
        _target_subject = f'{output.Subject.TARGET}{output.CliFormat.BLACK}[REMOTE]{output.CliFormat.ENDC} '
    elif not mode.is_remote(mode.Client.TARGET) and not mode.is_remote(mode.Client.ORIGIN):
        _origin_subject = f'{output.Subject.ORIGIN}{output.CliFormat.BLACK}[LOCAL]{output.CliFormat.ENDC} '
        _target_subject = f'{output.Subject.TARGET}{output.CliFormat.BLACK}[LOCAL]{output.CliFormat.ENDC} '

    _origin_name = helper.get_ssh_host_name(mode.Client.ORIGIN, True) if _remote_client == mode.Client.ORIGIN else ''
    _target_name = helper.get_ssh_host_name(mode.Client.TARGET, True) if _remote_client == mode.Client.TARGET else ''

    if not system.config['mute']:
        print(
            f'{_origin_subject}'
            f'{_origin_name}'
            f'{output.CliFormat.BLACK}{origin_path}{output.CliFormat.ENDC}'
        )

        print(
            f'{_target_subject}'
            f'{_target_name}'
            f'{output.CliFormat.BLACK}{target_path}{output.CliFormat.ENDC}'
        )

    _origin_user_host = utility.get_host(mode.Client.ORIGIN) if _remote_client == mode.Client.ORIGIN else ''
    _target_user_host = utility.get_host(mode.Client.TARGET) if _remote_client == mode.Client.TARGET else ''

    _output = mode.run_command(
        f'{utility.get_password_environment(_remote_client)}rsync {utility.get_options()} '
        f'{utility.get_authorization(_remote_client)} {utility.get_excludes(exclude)}'
        f'{_origin_user_host}{origin_path} {_target_user_host}{target_path}',
        client,
        True
    )
    utility.read_stats(_output)

