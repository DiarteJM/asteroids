from constants import ASTEROID_MIN_RADIUS
import pygame
import random
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None, speed=None):
        super().__init__(x, y, radius)
        self.velocity = velocity
        self.speed = random.uniform(0, 360)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        if self.velocity.length() == 0:
            velocity1 = pygame.Vector2(1, 0)
            velocity2 = pygame.Vector2(-1, 0)

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, velocity1)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, velocity2)
        new_asteroid1.add(*Asteroid.containers)
        new_asteroid2.add(*Asteroid.containers)