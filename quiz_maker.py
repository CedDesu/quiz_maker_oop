class QuizMaker:
    def __init__(self):
        self.user_quiz_data = []

    def start(self):
        input("Welcome to Quiz_Creator v.1, please press any button to start.\n")

        while True:
            self.add_question()

            next_question = input("Do you want to input another question? (yes/no)\n").strip().lower()
            if next_question not in ('yes', 'y'):
                break

        self.save_quiz_to_file()
        print("Your quiz has been created and saved into a .txt file. (Saved in the same folder as the quiz_creator code)")

    def add_question(self):
        question_text = input("Enter a question: \n")

        choices = {}
        for letter in ['a', 'b', 'c', 'd']:
            answer_text = input(f"Enter choice {letter}: ")
            choices[letter] = answer_text

        while True:
            correct_choice = input("Which choice is the correct answer?: (a/b/c/d)\n").strip().lower()
            if correct_choice in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Please type a valid input. (a/b/c/d)")

        question_entry = {
            "question": question_text,
            "choices": choices,
            "answers": correct_choice
        }

        self.user_quiz_data.append(question_entry)

    def save_quiz_to_file(self):
        with open("quiz.txt", "w") as file:
            for index, item in enumerate(self.user_quiz_data, 1):
                file.write(f"Q{index}: {item['question']}\n")
                for key in ['a', 'b', 'c', 'd']:
                    file.write(f"  {key}) {item['choices'][key]}\n")

                correct_answer_text = item['choices'][item['answers']]
                file.write(f"Correct answer: {item['answers']}) {correct_answer_text}\n\n")
