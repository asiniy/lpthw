from sys import exit
from random import choice
from stringcase import pascalcase

class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n-------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = [
        "You've died",
        "Such a luser",
        "I have a small puppy who's better than this"
    ]

    def enter(self):
        random_quip = choice(Death.quips)
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        #

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()
