import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGTH
from snake import *
from apple import *
def main():
    print("Hello to my first solo project")
    print("I am making the game snake")
    print("The objective is to have square on a screen a grows each time the snake eats an apple")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
    clock = pygame.time.Clock()
    running = True
    x_value = SCREEN_WIDTH//2
    y_value = SCREEN_HEIGTH/2
    #Snake Values
    apple_x_value = random.randint(0,1000)
    apple_y_value = random.randint(0,650)
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        snake = Snake(x_value,y_value,50,50,"red") 
        apple = Apple(apple_x_value,apple_y_value)
        screen.fill((0,135,62))
        snake.draw(screen)
        apple.draw(screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y_value -= 5
        if keys[pygame.K_s]:
            y_value += 5
        if keys[pygame.K_a]:
            x_value -= 5
        if keys[pygame.K_d]:
            x_value += 5
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
          main()
