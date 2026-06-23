import pygame
import random

class Food():
    def __init__(self):
        self.x = random.randint(0,720)
        self.y = random.randint(0,720)
    def draw(self,screen):
        food_list = []
        while len(food_list) <= 1:
           food_list.append((self.x,self.y,50,50))
        pygame.draw.rect(screen,"blue",food_list[0])
