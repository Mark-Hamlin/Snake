import pygame

class Snake:
    def __init__(self,x,y,width,height,color):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.height,self.width))
