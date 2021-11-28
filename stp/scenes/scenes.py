#!/usr/bin/env python3

from stp.sentences.sentences import Sentence
from stp.props.props import Prop
from stp.props.creatures import *
from stp.props.plants import *
import random

class Scene:

    name = ''

    ground = None
    creatures = []
    plants = []
    props = []

    light = 0

    def __init__(self):
        pass

    def reset(self):
        self.ground = None
        self.creatures = []
        self.plants = []
        self.props = []
        self.light = 0

    def describe(self):
        for prop in self.props:
            print('[ ' + prop.get('name') + ' ]: ' + prop.describe())

    def generate(self):
        self.reset()

        self.name = 'generated scene'

        grass = Prop('field of grass')
        grass.adjectives = ['lush','soft','green']
        self.ground = grass

        candle = Prop('candle')
        candle.adjectives = ['flickering', 'bright', 'lit']
        self.props.append(candle)

        candle = Prop('candle')
        candle.adjectives = ['extingushed', 'depleted', 'unlit']
        self.props.append(candle)

        flower = Prop('flower')
        flower.adjectives = ['beautiful', 'flourishing', 'blooming']
        self.props.append(flower)

        flower = Prop('flower')
        flower.adjectives = ['wilting', 'dying', 'neglected']
        self.props.append(flower)

        creature = creatures.Creature(['creature', 'critter'])
        creature.adjectives = ['peaceful','calm','meditative']
        creature.sit(self.ground)
        self.props.append(creature)

        tree = plants.Plant('tree', self.ground)
        tree.adjectives = ['deciduous','leafy','yellow']
        self.props.append(tree)

        crow = birds.Crow()
        crow.sit(tree)
        self.props.append(crow)

        crow = birds.Crow()
        crow.fly()
        self.props.append(crow)
