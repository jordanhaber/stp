#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop

class Bird(Prop):

    target = None
    ground = None
    sitting = False
    flying = True

    def __init__(self, name, adjectives = []):
        super().__init__(name, adjectives)
        self.descriptions = [Sentence(self, "It's {adjective}, {action}.")]

    def sit(self, target = None):
        self.ground = target
        self.sitting = True
        self.flying = False
        self.actions = ['sitting','perched','resting']
        if self.ground:
            sentence = "It's a {adjective} {name}, {action} on a " + self.ground.adjective() + " " + self.ground.name + "."
            sentence += " It's {verb} at you {adverb}."
            self.descriptions = [Sentence(self, sentence)]

    def fly(self, target = None):
        self.ground = target
        self.flying = True
        self.sitting = False
        self.actions = ['flying','fliting','gliding']
        replacements = {'emphasis': ['overhead', 'far above', 'aloft']}
        self.descriptions = [Sentence(self, "It's a {adjective} {name}, {action} {emphasis}.", replacements)]

class Crow(Bird):

    # descriptions.append = [{"The {adjective} {name} {action} {action_emphasis} you.":{action_emphasis}}]

    def __init__(self):
        super().__init__('crow', [])
        self.adjectives = ['shifty','ominous']
        self.verbs = ['staring','gazing','looking']
        self.adverbs = ['inquisitively','expectantly']
