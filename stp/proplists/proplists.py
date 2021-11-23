#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop
from stp.props.creatures import *
import random

class PropList:

    props = []

    def __init__(self):
        pass

    def reset(self):
        self.props = []

    def describe(self):
        for prop in self.props:
            #print('A ' + prop.name + '. ' + prop.describe())
            print('[ ' + prop.get('name') + ' ]: ' + prop.describe())

    def generate(self):
        self.reset()

        self.props.append(Prop('candle', ['flickering', 'bright', 'lit']))
        self.props.append(Prop('candle', ['extingushed', 'depleted', 'unlit']))

        self.props.append(Prop('flower', ['beautiful', 'flourishing', 'blooming']))
        self.props.append(Prop('flower', ['wilting', 'dying', 'neglected']))

        grass = Prop('patch of grass', ['dry','faded','dead'])
        self.props.append(grass)

        creature = creatures.Creature(['creature', 'critter'],['peaceful','calm','meditative'])
        creature.sit(grass)
        self.props.append(creature)

        tree = Prop('tree', ['deciduous','leafy','yellow'])
        self.props.append(tree)

        crow = birds.Crow()
        crow.sit(tree)
        self.props.append(crow)

        crow = birds.Crow()
        crow.fly()
        self.props.append(crow)
