#!/usr/bin/env python3

from stp.proplists.proplists import PropList

class Game:

    proplists = {}

    def __init__(self):
        pass

    def reset(self):
        self.proplists = {}

    def describe(self):
        for name in self.proplists:
            print('[ ' + name + ' ]')
            self.proplists[name].describe()
            print()

    def generate(self):
        self.reset()

        proplist = PropList()
        proplist.generate()
        self.proplists['generated prop list'] = proplist;
