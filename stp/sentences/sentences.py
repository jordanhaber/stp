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
            for token in re.finditer(r'(\{)([^\}]*)(\})', sentence):
                key = token.group(2)
                subkey = key.split('.')
                if len(subkey) > 1:
                    value = self.subject.get(subkey[0]).get(subkey[1])
                else:
                    value = self.subject.get(key)
                if value:
                    sentence = re.sub(r'\{' + key + '\}', value, sentence)

        if len(self.replacements):
            for key in self.replacements:
                replacement = random.choice(self.replacements[key])
                sentence = re.sub(r'\{' + key + '\}', replacement, sentence)

        if sentence[0].islower():
            sentence = sentence[0].upper() + sentence[1:]

        sentence = re.sub(r'(A| a) (a|e|i|o|u)', a_to_an, sentence)

        self.sentence = sentence

def a_to_an(match):
    char = match.group(1)
    return char + 'n ' + match.group(2)
