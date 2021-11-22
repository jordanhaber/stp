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
            print('A ' + prop.name + '. ' + prop.describe())

    def generate(self):
        self.reset()

        self.props.append(Prop('candle', ['flickering', 'bright', 'lit']))
        self.props.append(Prop('candle', ['extingushed', 'depleted', 'unlit']))

        self.props.append(Prop('flower', ['beautiful', 'flourishing', 'blooming']))
        self.props.append(Prop('flower', ['wilting', 'dying', 'neglected']))

        crow = birds.Bird('crow', ['shifty','shadowy','drab'])
        crow.verbs = ['staring','gazing','looking']
        crow.adverbs = ['inquisitively','expectantly']
        self.props.append(crow)
