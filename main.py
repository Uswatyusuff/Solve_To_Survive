import pygame
import time
import random

WIDTH, HEIGHT = 1250, 720

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solve To Survive")
# Load the image from the specified file path
image = pygame.image.load('background_image.jpg')


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
                # Check if a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Draw the image on the screen at the top-left corner (0, 0)
        WIN.blit(image, (0, 0))

        # Update the display
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()