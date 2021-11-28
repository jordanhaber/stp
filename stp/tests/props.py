#!/usr/bin/env python3

from stp.props.props import Prop

import unittest
import re

class TestSentences(unittest.TestCase):

    def test_add(self):
        parent = Prop('Parent')
        child = Prop('Child')
        parent.add(child)
        self.assertTrue(child.parent == parent)
        self.assertTrue(child in parent.children)

    def test_remove(self):
        parent = Prop('Parent')
        child = Prop('Child')
        parent.add(child)
        parent.remove(child)
        self.assertTrue(child.parent == None)
        self.assertFalse(child in parent.children)

if __name__ == '__main__':
    unittest.main()
