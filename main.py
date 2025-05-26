"""
Code for the two separate quiz .py files that creates an instance and runs the quiz_creator

"""

from quiz_maker import QuizMaker
from quiz_taker import QuizTaker

def main():
    print("1. Create a quiz")
    print("2. Take the quiz")
    choice = input("Select an option (1/2): ").strip()

    if choice == '1':
        quiz_creator = QuizMaker()
        quiz_creator.start()
    elif choice == '2':
        quiz_taker = QuizTaker("quiz.txt")
        quiz_taker.display_quiz_window()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
