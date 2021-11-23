#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop

class Creature(Prop):

    life = 100
    health = life

    target = None
    ground = None
    sitting = False

    def __init__(self, name, adjectives = []):
        super().__init__(name, adjectives)

    def sit(self, target):
        self.ground = target
        self.sitting = True
        self.actions = ['sitting','resting']
        replacements = {'emphasis': ['on a', 'upon a']}

        sentence = "It's a {adjective} {name}, {action} {emphasis} " + self.ground.get('adjectives') + " " + self.ground.name + "."
        self.descriptions = [Sentence(self, sentence, replacements)]
