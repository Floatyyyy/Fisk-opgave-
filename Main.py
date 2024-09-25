import pygame
from Vector import vector
from fish import Fish
from flock import Flock

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

num_fish = 15
flock = Flock(num_fish)



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