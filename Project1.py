class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question, options):
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
    
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    
    def run_quiz(self):
        for question, options, correct_answer in self.questions:
            self.display_question(question, options)
            user_answer = input("Enter your answer (by typing the option number): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                self.check_answer(options[int(user_answer) - 1], correct_answer)
            else:
                print("Invalid input. Please enter a valid option number.")
        print(f"Quiz ended. Your final score is {self.score}/{len(self.questions)}.")

questions = [
    ("What is the capital of France?", ["Paris", "Rome", "Berlin"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter"], "Mars"),
    ("Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Jane Austen", "Charles Dickens"], "William Shakespeare"),
    ("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"], "Pacific Ocean"),
    ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso"], "Leonardo da Vinci"),
    ("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "South Korea"], "Japan"),
    ("What is the chemical symbol for water?", ["Wa", "H2O", "O2"], "H2O")
]

quiz = Quiz(questions)
quiz.run_quiz()
