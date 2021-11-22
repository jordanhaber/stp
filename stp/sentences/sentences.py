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

        if len(self.subject.adjectives):
            adjective = random.choice(self.subject.adjectives)
            sentence = re.sub('\{adjective\}', adjective, sentence)

        if len(self.subject.adverbs):
            adverb = random.choice(self.subject.adverbs)
            sentence = re.sub('\{adverb\}', adverb, sentence)

        if len(self.subject.verbs):
            verb = random.choice(self.subject.verbs)
            sentence = re.sub('\{verb\}', verb, sentence)

        self.sentence = sentence
