import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_ROTATE_SPEED, PLAYER_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)


    def move(self, dt):
         forward = pygame.Vector2(0,1).rotate(self.rotation)
         self.position += forward * PLAYER_SPEED * dt


    def update(self, dt):
        self.position += (self.velocity * dt)
