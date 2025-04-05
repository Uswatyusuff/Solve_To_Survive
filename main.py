import pygame
from button import Button
from quiz_loader import QuizLoader

pygame.init()

WIDTH, HEIGHT = 1250, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solve To Survive")

my_font = pygame.font.SysFont('Comic Sans MS', 30)

# Load images
background_image = pygame.image.load('background_image.jpg')
monster = pygame.image.load('monster.png')
character = pygame.image.load('farmer_hamster.png')
monster = pygame.transform.scale(monster, (200, 200))
character = pygame.transform.scale(character, (200, 200))

# Load quiz questions
quiz = QuizLoader('level1.json')
current_question_data = quiz.next_question() if quiz.has_next() else None

# Set up question text and answer buttons
question_text = current_question_data["question"] if current_question_data else ""
answer_options = current_question_data["options"] if current_question_data else []
correct_answer = current_question_data["answer"] if current_question_data else ""

option_buttons = []
for i in range(4):
    option_text = answer_options[i] if i < len(answer_options) else ""
    option_buttons.append(Button((100, 200, 250), 480, 280 + i * 50, 300, 40, option_text))

# UI labels
monster_level_bar = my_font.render("Monster score: 5", True, (255, 255, 255))
character_level_bar = my_font.render("Player score: 5", True, (255, 255, 255))

# Text Rects
monster_text_rect = monster_level_bar.get_rect(center=(320, 260))
character_text_rect = character_level_bar.get_rect(center=(940, 260))

def main():
    global current_question_data, question_text, correct_answer

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for btn in option_buttons:
                    if btn.is_over(mouse_pos):
                        print(f"You clicked: {btn.text}")
                        if btn.text == correct_answer:
                            print("✅ Correct!")
                            # Load next question
                            if quiz.has_next():
                                current_question_data = quiz.next_question()
                                question_text = current_question_data["question"]
                                correct_answer = current_question_data["answer"]
                                for i, btn in enumerate(option_buttons):
                                    btn.text = current_question_data["options"][i]
                            else:
                                print("🎉 Quiz completed!")
                                run = False
                        else:
                            print("❌ Wrong!")

        # Drawing
        WIN.blit(background_image, (0, 0))
        WIN.blit(monster, (250, 400))
        WIN.blit(character, (850, 400))
        WIN.blit(monster_level_bar, monster_text_rect)
        WIN.blit(character_level_bar, character_text_rect)

        # Render updated question text
        question_surface = my_font.render(question_text, True, (255, 255, 255))
        question_text_rect = question_surface.get_rect(center=(640, 100))
        WIN.blit(question_surface, question_text_rect)

        for btn in option_buttons:
            btn.draw(WIN)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
