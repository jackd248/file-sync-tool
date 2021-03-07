#!/usr/bin/env python3
# -*- coding: future_fstrings -*-

from db_sync_tool.utility import system
from db_sync_tool.database import process
from file_sync_tool.utility import info, helper
from file_sync_tool.transfer import process


class Sync:
    """
    Synchronize target files from an origin system
    """

    def __init__(self,
                 config_file=None,
                 verbose=False,
                 mute=False,
                 host_file=None,
                 config={}):
        """
        Initialization
        :param config_file:
        :param verbose:
        :param mute:
        :param host_file:
        :param config:
        """
        info.print_header(mute)
        system.check_args_options(
            config_file=config_file,
            host_file=host_file,
            verbose=verbose,
            mute=mute
        )
        system.get_configuration(config)
        helper.adjust_sync_mode()
        helper.check_rsync_version()
        helper.check_sshpass_version()
        helper.check_authorizations()
        process.transfer_files()
        info.print_footer()
