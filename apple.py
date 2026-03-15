import pygame
import random
from constants import APPLE_WIDTH,APPLE_HEIGHT

class Apple:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = APPLE_WIDTH
        self.height = APPLE_HEIGHT
        self.color = "pink"
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
    
