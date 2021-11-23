#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop
from stp.props.creatures import *

class PropList:

    props = []

    def __init__(self):
        pass

    def reset(self):
        self.props = []

    def describe(self):
        for prop in self.props:
            #print('A ' + prop.name + '. ' + prop.describe())
            print('[ ' + prop.name + ' ]\t' + prop.describe())

    def generate(self):
        self.reset()

        test = Prop('"a" to "an"', ['abyssal', 'endearing', 'invincible', 'opaque', 'unbiased'])
        test.descriptions = [Sentence(test, "It's a {adjective} test.")]
        self.props.append(test)

        test = Prop('"a" to "an"', ['abyssal', 'endearing', 'invincible', 'opaque', 'unbiased'])
        test.descriptions = [Sentence(test, "A {adjective} test.")]
        self.props.append(test)

        self.props.append(Prop('candle', ['flickering', 'bright', 'lit']))
        self.props.append(Prop('candle', ['extingushed', 'depleted', 'unlit']))

        self.props.append(Prop('flower', ['beautiful', 'flourishing', 'blooming']))
        self.props.append(Prop('flower', ['wilting', 'dying', 'neglected']))

        tree = Prop('tree', ['deciduous','leafy','yellow'])
        self.props.append(tree)

        crow = birds.Crow()
        crow.sit(tree)
        self.props.append(crow)

        crow = birds.Crow()
        crow.fly()
        self.props.append(crow)
