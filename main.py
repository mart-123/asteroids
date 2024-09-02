import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


# the pythonic way to prevent running if imported as a module
if __name__ == "__main__":
    main()
