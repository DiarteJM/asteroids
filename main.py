import pygame
import sys
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from constants import *
from shot import Shot


def main():
    pygame.init()
    timer = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, 0)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

        screen.fill((0, 0, 0))
        dt = timer.tick(60) / 1000.0
        updatable.update(dt)
        for asteroid in asteroids:
            collides_with_ship = asteroid.collision_check(player)
            if collides_with_ship == True:
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                collides_with_asteroid = bullet.collision_check(asteroid)
                if collides_with_asteroid == True:
                    print("Bullet hit an asteroid!")
                    bullet.kill()
                    asteroid.split()
            
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
