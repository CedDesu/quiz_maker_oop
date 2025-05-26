def quiz_creator():
    user_quiz_data = []

    input("Welcome to Quiz_Creator v.1, please press any button to start.\n")

    #Asks the user for a question and 4 choices
    while True:
        input_question = input("Enter a question: \n")

        choices = {}
        for choice in ['a', 'b', 'c', 'd']:
            answer = input(f"Enter choice {choice}: ")
            choices[choice] = answer

        while True:
            correct_answer = input("Which choice is the correct answer?: (a/b/c/d)\n").strip().lower()
            if correct_answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Please type a valid input. (a/b/c/d)")

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

if __name__ == "__main__":
    quiz_creator()
