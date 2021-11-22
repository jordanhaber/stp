#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop

class Bird(Prop):

    action = 'perching'

    def __init__(self, name, adjectives = []):
        super().__init__(name, adjectives)
        self.descriptions = [Sentence(self, "It's {adjective}, and {verb} at you {adverb}.")]

class Crow(Bird):

    action = 'perching'
    # descriptions.append = [{"The {adjective} {name} {action} {action_emphasis} you.":{action_emphasis}}]

    def __init__(self, name, adjectives = []):
        super().__init__(name, adjectives)
        self.descriptions = [Sentence(self, "The {name} is {action}, {verb} at you {adverb}.")]
