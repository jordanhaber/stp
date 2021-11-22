#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
import random

class Prop:

    descriptions = []
    adjectives = []
    adverbs = []
    verbs = []

    def __init__(self, name, adjectives = []):
        self.name = name
        self.adjectives = adjectives
        self.descriptions = [Sentence(self, "It's {adjective}.")]

    def describe(self):
        description = random.choice(self.descriptions)
        return description.write()
