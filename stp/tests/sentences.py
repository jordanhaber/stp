#!/usr/bin/env python3

from stp.sentences.sentences import Sentence

import unittest
import re

class TestSentences(unittest.TestCase):

    def test_subject(self):
        subject = Object()
        subject.name = 'test'
        self.assertEqual(Sentence(subject, '{name}').write(), 'test')

    def test_replacements(self):
        self.assertEqual(Sentence(None, '{replace}', {'replace': ['replaced']}).write(), 'replaced')

    def test_a_to_an(self):
        self.assertEqual(Sentence(None, 'A a').write(), 'An a')
        self.assertEqual(Sentence(None, ' a a').write(), ' an a')

class Object():
    pass

if __name__ == '__main__':
    unittest.main()
