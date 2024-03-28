import requests

class Quiz:
    def __init__(self):
        self.score = 0

    def start(self, num_questions):
        for i in range(num_questions):
            self.get_question()
            self.display_question()
            self.check_answer(input("Enter your answer: "))

    def get_question(self):
        response = requests.get("https://opentdb.com/api.php?amount=1&category=28&type=multiple")
        data = response.json()
        if 'results' in data:
            question_data = data['results'][0]
            self.question = question_data['question']
            self.incorrect_answers = question_data['incorrect_answers']
            self.correct_answer = question_data['correct_answer']
            self.choices = self.incorrect_answers + [self.correct_answer]
        else: 
            print("Can Your Computer Not Handle This Code Or Something?")

    def display_question(self):
        print(self.question)
        for index, choice in enumerate(self.choices, 1):
            print(f"{index}{choice}")

    def check_answer(self, choice):
        index = int(choice) - 1
        if self.choices[index] == self.correct_answer:
            self.score += 1
            print("Lucky Guess I Suppose, Your Score Is Now:", self.score)
        else:
            print("Womp Womp, The Correct Answer Was:", self.correct_answer)

if __name__ == "__main__":
    print("Welcome To The Passive Aggressive Vehicles Test! Do You Really Think You Have What It Takes?")
    num_questions = int(input("How Many Questions Would You Like To Attempt? ")) 
    print(f"Wow, Only {num_questions} Are You Serious? Ok Then...\n")
    quiz = Quiz()
    quiz.start(num_questions)
