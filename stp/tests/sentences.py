#!/usr/bin/env python3

from stp.sentences.sentences import Sentence

import unittest
import re

class TestSentences(unittest.TestCase):

    def test_capitalization(self):
        self.assertEqual(Sentence(None, 'capitalize').write(), 'Capitalize')

    def test_a_to_an(self):
        self.assertEqual(Sentence(None, 'A a').write(), 'An a')
        self.assertEqual(Sentence(None, ' a a').write(), ' an a')

    def test_subject(self):
        subject = Object()
        subject.name = 'test'
        self.assertEqual(Sentence(subject, '{name}').write(), 'Test')

    def test_no_subject(self):
        self.assertEqual(Sentence(None, '{name}').write(), '{name}')

    def test_replacements(self):
        self.assertEqual(Sentence(None, '{replace}', {'replace': ['replaced']}).write(), 'Replaced')

class Object():
    pass

if __name__ == '__main__':
    unittest.main()
