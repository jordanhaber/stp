#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop

import unittest
import re

class TestSentences(unittest.TestCase):

    def test_capitalization(self):
        self.assertEqual(Sentence(None, 'capitalize').write(), 'Capitalize')

    def test_a_to_an(self):
        self.assertEqual(Sentence(None, 'A a').write(), 'An a')
        self.assertEqual(Sentence(None, ' a a').write(), ' an a')

    def test_subject(self):
        subject = Prop('test')
        self.assertEqual(Sentence(subject, '{name}').write(), 'Test')

    def test_no_subject(self):
        self.assertEqual(Sentence(None, '{name}').write(), '{name}')

    def test_nested_subject(self):
        subject = Prop('Test Child')
        parent = Prop('Test Parent')
        parent.add(subject)
        self.assertEqual(Sentence(subject, '{parent.name}').write(), 'Test Parent')

    def test_replacements(self):
        self.assertEqual(Sentence(None, '{replace}', {'replace': ['replaced']}).write(), 'Replaced')

if __name__ == '__main__':
    unittest.main()
