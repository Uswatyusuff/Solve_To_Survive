import pygame
import time
import random

WIDTH, HEIGHT = 500, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solve To Survive")



def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()


if __name__ == "__main__":
    main()