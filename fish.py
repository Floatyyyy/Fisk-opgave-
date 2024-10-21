import pygame
from Vector import *
import random

class Fish:
    def __init__(self, position, velocity,screen):
        self.screen = screen
        self.position = position
        self.velocity = velocity
        fish_img = ["Fisk.png","Squid.png","Shark.png"]
        scaled_fish_img = [pygame.transform.scale(pygame.image.load(img), (50,50)) for img in fish_img]

        self.fish_img =  random.choice(scaled_fish_img)


    def update(self):
        
        self.position = self.position + self.velocity
        
    def screenConfinment(self):
        if self.position.x <= 0 or self.position.x >= self.screen.get_width():
            self.velocity.x = -self.velocity.x
        if self.position.y <= 0 or self.position.y >= self.screen.pygame.Surface.get_height():
            self.velocity.y = -self.velocity.y

    def draw(self, screen):
        screen.blit(self.fish_img, (self.position.x, self.position.y))



