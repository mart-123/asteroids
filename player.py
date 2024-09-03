import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_ROTATE_SPEED, PLAYER_SPEED
from constants import PLAYER_BULLET_SPEED, PLAYER_SHOOT_COOLDOWN
from bullet import Bullet

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.latest_shot_timer = 0.00
    

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_ROTATE_SPEED * dt)
    
    def move(self, dt):
         forward = pygame.Vector2(0,1).rotate(self.rotation)
         self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.latest_shot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1.00)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1.00)
        if keys[pygame.K_SPACE] and self.latest_shot_timer <= 0.0:
            self.shoot()
        
    def shoot(self):
        bullet_vector = pygame.Vector2(0,1).rotate(self.rotation)
        bullet_velocity = bullet_vector * PLAYER_BULLET_SPEED
        bullet = Bullet(self.position.x, self.position.y, bullet_velocity)

        self.latest_shot_timer = PLAYER_SHOOT_COOLDOWN

