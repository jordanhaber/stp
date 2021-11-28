#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop

class Plant(Prop):

    life = 100
    health = life

    planted = True

    def __init__(self, name):
        super().__init__(name)
        self.descriptions = [Sentence(self, "It's {adjective}, growing out of a {parent.name}.")]

    def plant(self, target):
        target.add(self)
        self.planted = True
