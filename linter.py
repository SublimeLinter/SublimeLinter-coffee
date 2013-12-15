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

from SublimeLinter.lint import Linter, persist


class Coffee(Linter):

    """Provides an interface to coffee --compile."""

    syntax = ('coffeescript', 'coffeescript_literate')
    executable = 'coffee'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>error)|(?P<warning>warning)): (?P<message>[^\r\n]+)'
    )
    comment_re = r'\s*/[/*]'

    def cmd(self):
        """Return a list with the command line to execute."""

        result = ['coffee', '--compile', '--stdio']

        if persist.get_syntax(self.view) == 'coffeescript_literate':
            result.append('--literate')

        return result
