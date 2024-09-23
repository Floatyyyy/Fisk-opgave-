import pygame
from Vector import vector
from fish import Fish
from flock import Flock

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

fish_img = ["Fisk.png","Squid.png","Shark.png"]
scaled_fish_img = [pygame.transform.scale(pygame.image.load(img), (35,35)) for img in fish_img]

num_fish = 15
flock = Flock(num_fish, fish_img)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    flock.update()

    screen.fill((0, 128, 255))

    flock.draw(screen)
    for i, fish in enumerate(flock.fish_list):
        print(f"Fisk {i + 1}: {fish.position}")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()