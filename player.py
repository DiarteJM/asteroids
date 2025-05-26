import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

class Player(CircleShape):
  def __init__(self, x, y, radius, rotation):
    super().__init__(x, y, PLAYER_RADIUS)
    self.__rotation = rotation

  def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.__rotation)
      right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
  
  def draw(self, screen):
     pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

  def rotate(self, dt):
     self.__rotation += (PLAYER_TURN_SPEED * dt)

  def move(self, dt):
      # start with unit vector pointing straight up from (0, 0) to (0, 1)
      # rotate that vector by the player's rotation
      forward = pygame.Vector2(0, 1).rotate(self.__rotation)
      # multiply by PLAYER_SPEED * dt; larger vector means faster speed
      # add vector to our position to move player
      self.position += forward * PLAYER_SPEED * dt
      
  def update(self, dt):
      keys = pygame.key.get_pressed()

      if keys[pygame.K_a]:
        self.rotate(-dt)
      if keys[pygame.K_d]:
        self.rotate(dt)
      if keys[pygame.K_w]:
        self.move(dt)
      if keys[pygame.K_s]:
        self.move(-dt)
      
    
    