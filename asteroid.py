import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_SPEED, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)


    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        # generate two new asteroids: smaller, faster, one left, one right
        split_angle = random.uniform(20, 50)
        split_left_velocity = self.velocity.rotate(split_angle * -1.0) * 1.2
        split_right_velocity = self.velocity.rotate(split_angle) * 1.2
        split_size = self.radius - ASTEROID_MIN_RADIUS

        asteroid_left = Asteroid(self.position.x, self.position.y, split_size)
        asteroid_right = Asteroid(self.position.x, self.position.y, split_size)
        asteroid_left.velocity = split_left_velocity
        asteroid_right.velocity = split_right_velocity

