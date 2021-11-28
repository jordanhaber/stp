#!/usr/bin/env python3

from stp.scenes.scenes import Scene

class Game:

    scenes = []
    scene = None

    def __init__(self):
        pass

    def reset(self):
        self.scenes = []

    def describe(self):
        print()
        for scene in self.scenes:
            print('[ ' + scene.name + ' ]')
            print()
            scene.describe()
            print()
            print()

    def generate(self):
        self.reset()

        scene = Scene()
        scene.generate()
        self.scenes.append(scene);
