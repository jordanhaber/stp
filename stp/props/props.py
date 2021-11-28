#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
import random

class Prop:

    parent = None
    children = []

    def __init__(self, name, adjectives = []):
        self.name = name
        self.adjectives = adjectives
        self.descriptions = [Sentence(self, "It's {adjective}.")]

    def describe(self):
        description = random.choice(self.descriptions)
        return description.write()

    def add(self, prop):
        self.children.append(prop)
        prop.parent = self

    def get(self, key):
        try:
            value = getattr(self, key)
        except AttributeError:
            try:
                value = getattr(self, key + 's')
            except AttributeError:
                return None

        if type(value) is list:
            try:
                return random.choice(value)
            except IndexError:
                return None

        return value
