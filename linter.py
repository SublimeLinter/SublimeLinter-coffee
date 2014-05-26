#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Coffee plugin class."""

from SublimeLinter.lint import Linter, util


class Coffee(Linter):

    """Provides an interface to coffee --compile."""

    syntax = 'coffeescript'
    cmd = 'coffee --compile --stdio'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.5'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>error)|(?P<warning>warning)): (?P<message>[^\r\n]+)'
    )
    error_stream = util.STREAM_STDERR
    comment_re = r'\s*/[/*]'
