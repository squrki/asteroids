from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle_1 = self.velocity.rotate(random.random())
        angle_2 = -angle_1
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
        ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
        ast_1.velocity = angle_1*1.2
        ast_2.velocity = angle_2*1.2