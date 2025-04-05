import pygame
from button import Button
from quiz_loader import QuizLoader

pygame.init()

WIDTH, HEIGHT = 1250, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solve To Survive")

my_font = pygame.font.SysFont('Comic Sans MS', 30)

# Game state
level_counter = 1
monster_original_score = 5
character_original_score = 5

# Load images
background_image = pygame.image.load('background_image.jpg')
character = pygame.image.load('farmer_hamster.png')
character = pygame.transform.scale(character, (200, 200))

def load_monster_image(path: str, size=(200, 200)):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)

def load_quiz(path: str):
    quiz = QuizLoader(path)
    current_question_data = quiz.next_question() if quiz.has_next() else None

    question_text = current_question_data["question"] if current_question_data else ""
    answer_options = current_question_data["options"] if current_question_data else []
    correct_answer = current_question_data["answer"] if current_question_data else ""

    option_buttons = []
    for i in range(4):
        option_text = answer_options[i] if i < len(answer_options) else ""
        option_buttons.append(Button((100, 200, 250), 480, 280 + i * 50, 300, 40, option_text))

    return quiz, current_question_data, question_text, correct_answer, option_buttons

def get_level_path(level):
    return f'level{level}.json'

def get_monster_path(level):
    return 'monster2.png' if level > 1 else 'monster.png'

def main():
    global level_counter, monster_original_score, character_original_score

    # Initial level load
    monster = load_monster_image(get_monster_path(level_counter))
    quiz, current_question_data, question_text, correct_answer, option_buttons = load_quiz(get_level_path(level_counter))

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
                            monster_original_score -= 1
                            if quiz.has_next():
                                current_question_data = quiz.next_question()
                                question_text = current_question_data["question"]
                                correct_answer = current_question_data["answer"]
                                for i, btn in enumerate(option_buttons):
                                    btn.text = current_question_data["options"][i]
                            else:
                                print("🎉 Level completed!")
                                level_counter += 1
                                if level_counter > 5:
                                    print("🏆 All levels complete!")
                                    run = False
                                else:
                                    # Load next level
                                    monster_original_score = 5
                                    character_original_score = 5
                                    monster = load_monster_image(get_monster_path(level_counter))
                                    quiz, current_question_data, question_text, correct_answer, option_buttons = load_quiz(get_level_path(level_counter))
                        else:
                            print("❌ Wrong!")
                            character_original_score -= 1

        # Drawing
        WIN.blit(background_image, (0, 0))
        WIN.blit(monster, (250, 400))
        WIN.blit(character, (850, 400))

        # Render updated question text
        question_surface = my_font.render(question_text, True, (255, 255, 255))
        question_text_rect = question_surface.get_rect(center=(640, 100))

        monster_level_bar = my_font.render(f"Monster score: {monster_original_score}", True, (255, 255, 255))
        character_level_bar = my_font.render(f"Player score: {character_original_score}", True, (255, 255, 255))

        # Text Rects
        monster_text_rect = monster_level_bar.get_rect(center=(320, 260))
        character_text_rect = character_level_bar.get_rect(center=(940, 260))

        WIN.blit(question_surface, question_text_rect)
        WIN.blit(monster_level_bar, monster_text_rect)
        WIN.blit(character_level_bar, character_text_rect)

        for btn in option_buttons:
            btn.draw(WIN)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
