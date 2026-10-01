import importlib
import unittest

import sublime
from SublimeLinter.lint.linter import VirtualView


Linter = importlib.import_module('SublimeLinter-coffee.linter').Coffee


class TestColumns(unittest.TestCase):
    def test_issue_6_examples(self):
        for source, column in [('s = "😀😀" ; foo bar baz(\n', 25),
                               ('x = "é😀" + (1 +\ny = 2\n', 13)]:
            with self.subTest(source=source):
                self.assertMatch('[stdin]:1:{}: error: missing )'.format(column), source)

    def test_near_line_end_columns_are_converted_before_clamping(self):
        self.assertMatch('[stdin]:1:37: error: missing )', 's = "😀😀😀😀😀😀😀😀" ; foo bar baz(\n')

    def test_ascii_columns_are_unchanged(self):
        self.assertMatch('[stdin]:1:4: error: missing )', 'baz(\n')

    def assertMatch(self, output, source):
        linter = Linter(sublime.View(0), {})
        match, = linter.find_errors(output)
        error = linter.process_match(match, VirtualView(source))
        self.assertIsNotNone(error)
        col = source.index('(')
        self.assertEqual({k: error[k] for k in ('line', 'start', 'region', 'offending_text')}, {
            'line': 0, 'start': col, 'region': sublime.Region(col, col + 1), 'offending_text': '(',
        })
