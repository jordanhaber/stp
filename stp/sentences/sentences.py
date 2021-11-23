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

        if self.subject:
            sentence = re.sub(r'\{name\}', self.subject.name, sentence)

            if hasattr(self.subject, 'adjectives') and len(self.subject.adjectives):
                adjective = random.choice(self.subject.adjectives)
                sentence = re.sub(r'\{adjective\}', adjective, sentence)

            if hasattr(self.subject, 'adverbs') and len(self.subject.adverbs):
                adverb = random.choice(self.subject.adverbs)
                sentence = re.sub(r'\{adverb\}', adverb, sentence)

            if hasattr(self.subject, 'verb') and len(self.subject.verbs):
                verb = random.choice(self.subject.verbs)
                sentence = re.sub(r'\{verb\}', verb, sentence)

            if hasattr(self.subject, 'action') and len(self.subject.actions):
                action = random.choice(self.subject.actions)
                sentence = re.sub(r'\{action\}', action, sentence)

        if len(self.replacements):
            for key in self.replacements:
                replacement = random.choice(self.replacements[key])
                sentence = re.sub(r'\{' + key + '\}', replacement, sentence)

        sentence = re.sub(r'(A| a) (a|e|i|o|u)', a_to_an, sentence)
        self.sentence = sentence

def a_to_an(match):
    char = match.group(1)
    return char + 'n ' + match.group(2)
