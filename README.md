SublimeLinter-coffee
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-coffee.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-coffee)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to the [coffeescript compiler](http://coffeescript.org). It will be used with files that have the “CoffeeScript” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `coffee` (1.5 or later) is installed on your system. To install `coffee`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `coffee` by typing the following in a terminal:
   ```
   npm install -g coffee-script
   ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.


### Linter configuration
In order for `coffee` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
