#!/usr/bin/env python3

import random
import re

class Sentence:

    sentence = ''

    def __init__(self, subject, structure, replacements = {}):
        self.subject = subject
        self.structure = structure
        self.replacements = replacements

    def write(self):
        if not len(self.sentence):
            self.generate()
        return self.sentence

    def generate(self):
        sentence = self.structure

        sentence = re.sub('\{name\}', self.subject.name, sentence)

        if len(self.subject.adjectives):
            adjective = random.choice(self.subject.adjectives)
            sentence = re.sub('\{adjective\}', adjective, sentence)

        if len(self.subject.adverbs):
            adverb = random.choice(self.subject.adverbs)
            sentence = re.sub('\{adverb\}', adverb, sentence)

        if len(self.subject.verbs):
            verb = random.choice(self.subject.verbs)
            sentence = re.sub('\{verb\}', verb, sentence)

        if len(self.subject.actions):
            action = random.choice(self.subject.actions)
            sentence = re.sub('\{action\}', action, sentence)

        if len(self.replacements):
            for key in self.replacements:
                replacement = random.choice(self.replacements[key])
                sentence = re.sub('\{' + key + '\}', replacement, sentence)

        self.sentence = sentence
