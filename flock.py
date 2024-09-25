import pygame, random
from Vector import *
from fish import * 


class Flock:
    def __init__(self, num_fish):
        self.fish_list = []
        for _ in range(num_fish):
            position = vector(random.randint(0, 800), random.randint(0, 600))
            velocity = vector(random.uniform(-1, 1), random.uniform(-1, 1))
            self.fish_list.append(Fish(position, velocity))

    def update(self):
        for fish in self.fish_list:
            fish.update()

    def draw(self, screen):
        for fish in self.fish_list:
            fish.draw(screen)

