from player import Player
import pygame
from constants import *


def main():
    pygame.init()
    timer = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, 0)
    
        
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return None

      screen.fill((0, 0, 0))
      dt = timer.tick(60) / 1000.0
      updatable.update(dt)
      for drawing in drawable:
          drawing.draw(screen)
      pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()