import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGTH
def main():
    print("Hello to my first solo project")
    print("I am making the game snake")
    print("The objective is to have square on a screen a grows each time the snake eats an apple")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("purple")
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
          main()
