import pygame
pygame.init()

WIDTH, HEIGHT = 1250, 720

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solve To Survive")

my_font = pygame.font.SysFont('Comic Sans MS', 30)

# Load the image from the specified file path
background_image = pygame.image.load('background_image.jpg')

monster = pygame.image.load('monster.png')
character = pygame.image.load('farmer_hamster.png')
monster= pygame.transform.scale(monster, (200, 200))
character = pygame.transform.scale(character, (200, 200))

# Render the text (text, antialias, color)
monster_level_bar = my_font.render("Monster score: 5", True, (255, 255, 255))  # White text
character_level_bar = my_font.render("Player score: 5", True, (255, 255, 255))

# Get a rect for positioning
monster_text_rect = monster_level_bar.get_rect(center=(320, 260))  # Center of the screen
character_text_rect = monster_level_bar.get_rect(center=(940, 260))

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
        WIN.blit(background_image, (0, 0))
        WIN.blit(monster, (250, 400))
        WIN.blit(character, (850, 400))
        WIN.blit(monster_level_bar, monster_text_rect)
        WIN.blit(character_level_bar, character_text_rect)
        # Update the display
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()