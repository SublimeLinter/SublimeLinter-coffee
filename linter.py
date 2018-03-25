from SublimeLinter.lint import Linter, util


class Coffee(Linter):
    cmd = 'coffee --compile --stdio'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>error)|(?P<warning>warning)): (?P<message>[^\r\n]+)'
    )
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.coffee'
    }
