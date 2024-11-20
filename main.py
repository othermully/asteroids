import pygame
from pygame.time import Clock
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids,updatables,drawables)
    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatables:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_detection(player):
                print("Game over!")
                pygame.quit()

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision_detection(asteroid):
                    bullet.kill()
                    asteroid.split()
 
        screen.fill("black")

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
