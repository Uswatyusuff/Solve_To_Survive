import json
from typing import List, Dict

class QuizLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.questions: List[Dict] = []
        self.current_index = 0
        self.load_questions()

    def load_questions(self):
        """Loads questions from the JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.questions = data.get("questions", [])
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading questions: {e}")
            self.questions = []

    def has_next(self):
        """Check if there are more questions."""
        return self.current_index < len(self.questions)

    def next_question(self):
        """Returns the next question dictionary and advances index."""
        if self.has_next():
            question = self.questions[self.current_index]
            self.current_index += 1
            return question
        return {}

    def reset(self):
        """Resets the quiz to the first question."""
        self.current_index = 0
