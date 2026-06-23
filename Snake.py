import pygame
import random
class Snake():
    def __init__(self):
        self.x = random.randint(0,720)
        self.y = random.randint(0,720)
        self.direction = None
    def draw(self,screen):
        pygame.draw.rect(screen,"red",(self.x,self.y,10,10))
    def move_up(self,dt):
        self.y -= 10 * dt
        if self.y <= 0:
            self.y = 0
    def move_down(self,dt):
        self.y += 10 * dt
        if self.y >= 1270:
            self.y = 0 
    def move_left(self,dt):
        self.x -= 10 * dt
        if self.x <= 0:
            self.x = 0
    def move_right(self,dt):
        self.x += 10 * dt
        if self.x >= 1270:
            self.x = 0
    def move(self,dt):
        if self.direction == "up":
            self.move_up(dt)
        elif self.direction == "down":
            self.move_down(dt)
        elif self.direction == "left":
            self.move_left(dt)
        elif self.direction == "right":
            self.move_right(dt)