import pygame
from constants import *
from Snake import *
from Food import *
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
snake = Snake()
food = Food()
running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill("green")
    snake.draw(screen)
    food.draw(screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and snake.direction != "down":
        snake.direction = "up"
    if keys[pygame.K_s] and snake.direction != "up":
        snake.direction = "down"
    if keys[pygame.K_a] and snake.direction != "right":
        snake.direction = "left"
    if keys[pygame.K_d] and snake.direction != "left":
        snake.direction = "right"
    snake.move(dt)

    pygame.display.flip()
    dt = clock.tick(60) / 100
    

pygame.quit()