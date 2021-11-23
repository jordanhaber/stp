#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.creatures.creatures import Creature

class Bird(Creature):

    target = None
    ground = None
    sitting = False
    flying = False

    def __init__(self, name, adjectives = []):
        super().__init__(name, adjectives)
        self.fly()
        self.descriptions = [Sentence(self, "It's {adjective}, {action}.")]

    def sit(self, target):
        super().sit(target)
        self.flying = False
        self.actions = ['sitting','perched','resting']
        replacements = {'emphasis': ['on a', 'upon a', 'gingerly on a']}

        sentence = "It's a {adjective} {name}, {action} {emphasis} " + self.ground.get('adjectives') + " " + self.ground.name + "."
        sentence += " It's {verb} at you {adverb}."
        self.descriptions = [Sentence(self, sentence, replacements)]

        sentence = "{action} {emphasis} " + self.ground.get('adjectives') + " " + self.ground.name + ", the {adjective} {name} is {verb} at you {adverb}."
        self.descriptions.append(Sentence(self, sentence, replacements))

    def fly(self, target = None):
        self.ground = target
        self.flying = True
        self.sitting = False
        self.actions = ['flying','fliting','gliding']
        replacements = {'emphasis': ['overhead', 'far above', 'aloft']}

        self.descriptions = [Sentence(self, "It's a {adjective} {name}, {action} {emphasis}.", replacements)]

class Crow(Bird):

    def __init__(self):
        super().__init__('crow', [])
        self.adjectives = ['shifty','ominous','proud']
        self.verbs = ['staring','gazing','looking']
        self.adverbs = ['inquisitively','expectantly']
