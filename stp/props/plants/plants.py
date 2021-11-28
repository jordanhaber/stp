#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop

class Plant(Prop):

    life = 100
    health = life

    target = None
    planted = True

    def __init__(self, name, ground):
        super().__init__(name)
        ground.add(self)
        self.planted = True
        self.descriptions = [Sentence(self, "It's {adjective}, growing out of a {parent.name}.")]
