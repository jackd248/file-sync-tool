#!/usr/bin/env python3
# -*- coding: future_fstrings -*-

from db_sync_tool.utility import output
from file_sync_tool import info


def print_header(mute):
    """
    Printing console header
    :param mute: Boolean
    :return:
    """
    if mute is False:
        print(output.CliFormat.BLACK + '##############################################' + output.CliFormat.ENDC)
        print(output.CliFormat.BLACK + '#                                            #' + output.CliFormat.ENDC)
        print(
            output.CliFormat.BLACK + '#' + output.CliFormat.ENDC + '               FILE SYNC TOOL               ' + output.CliFormat.BLACK + '#' + output.CliFormat.ENDC)
        print(output.CliFormat.BLACK + '#                  v' + info.__version__ + '                    #' + output.CliFormat.ENDC)
        print(output.CliFormat.BLACK + '# ' + info.__homepage__ + ' #' + output.CliFormat.ENDC)
        print(output.CliFormat.BLACK + '#                                            #' + output.CliFormat.ENDC)
        print(output.CliFormat.BLACK + '##############################################' + output.CliFormat.ENDC)


def print_footer():
    """
    Printing console footer
    :return:
    """
    _message = 'Successfully synchronized files'

    output.message(
        output.Subject.INFO,
        _message,
        True,
        True
    )