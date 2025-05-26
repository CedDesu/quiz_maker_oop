class QuizCreator:
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



            user_quiz_data.append({
                "question": input_question,
                "choices": choices,
                "answers": correct_answer
            })
            #Asks user which of the four choices is the correct answer.
            next_question = input("Do you want to input another question? (yes/no)\n").strip().lower()
            if next_question not in ('yes','y'):
                break

        #writes the user inputs into a .txt file
        with open("quiz.txt", "w") as f:
            for idx, item in enumerate(user_quiz_data, 1):
                f.write(f"Q{idx}: {item['question']}\n")
                for key in ['a', 'b', 'c', 'd']:
                    f.write(f"  {key}) {item['choices'][key]}\n")

                correct_answer = item['choices'][item['answers']]
                f.write(f"Correct answer: {item['answers']}) {correct_answer}\n")
                f.write("\n")

        print("Your quiz has been created and saved into a .txt file. (Saved in the same folder as the quiz_creator code)")


