import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # initialise pygame and basic config
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time in seconds

    # set up groups    
    grp_updatable = pygame.sprite.Group()
    grp_drawable = pygame.sprite.Group()
    grp_asteroids = pygame.sprite.Group()
    grp_bullets = pygame.sprite.Group()
    Player.containers = (grp_updatable, grp_drawable)
    Asteroid.containers = (grp_updatable, grp_drawable, grp_asteroids)
    AsteroidField.containers = (grp_updatable)
    Bullet.containers = (grp_updatable, grp_drawable, grp_bullets)

    # initiate objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # main loop
    while True:
        for event in pygame.event.get():    # check for window closed
            if event.type == pygame.QUIT:
                return
        
        for obj in grp_updatable:           # 'update' manipulates vectors and velocities
            obj.update(dt)
        
        print(f"asteroid group contains: {grp_asteroids}")
        for asteroid in grp_asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                raise SystemExit()

        screen.fill((0,0,0))
        for obj in grp_drawable:            # draw all sprites
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


# the pythonic way to prevent running if imported as a module
if __name__ == "__main__":
    main()
