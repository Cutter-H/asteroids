import pygame
from player import Player
from constants import *

def main():
    pygame.init()

    # Display screen settings.
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Setup screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x= SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, rotation=0)
    dt = 0
    
    # Main game loop
    while True:
        screen.fill(color="black")
        
        player.draw(screen)  
        
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(FRAMERATE) / 1000


if __name__ == "__main__":
    main()

