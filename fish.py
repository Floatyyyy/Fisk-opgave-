import pygame
from Vector import *

class Fish:
    def __init__(self, position, velocity, fish_img):
        self.position = position
        self.velocity = velocity
        self.fish_img = fish_img


    def update(self):
        
        self.position = self.position + self.velocity
        
    def screenConfinment(self):
        velocity = self.velocity
        if self.position.x <= 0 or self.position.x >= 800:
            self.velocity.x = -self.velocity.x
        if self.position.y <= 0 or self.position.y >= 600:
            self.velocity.y = -self.velocity.y

    def draw(self, screen):
        screen.blit(self.fish_img, (self.position.x, self.position.y))



