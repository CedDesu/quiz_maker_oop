"""
Quiz taker - 2nd part of quiz creator which uses tkinter library to open a new window for answering the made quiz
Status: Finished
"""

import tkinter as tk

class QuizTaker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.questions_data = self.load_questions_from_file()
        self.selected_answer_vars = []
        self.radio_button_groups = []

    def load_questions_from_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]

        questions_data = []
        for index in range(0, len(lines), 6):
            if lines[index].startswith("Q") and lines[index + 5].startswith("Correct answer:"):
                question_text = lines[index]
                choices = lines[index + 1 : index + 5]
                correct_answer_line = lines[index + 5]
                questions_data.append((question_text, choices, correct_answer_line))
        return questions_data

    def display_quiz_window(self):
        window = tk.Tk()
        window.title("Interactive Quiz")

        canvas = tk.Canvas(window)
        scrollbar = tk.Scrollbar(window, command=canvas.yview)
        question_container = tk.Frame(canvas)

        canvas.create_window((0, 0), window=question_container, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        question_container.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        for question_index, (question_text, choices_list, correct_answer_line) in enumerate(self.questions_data):
            correct_full_text = correct_answer_line.split(":", 1)[1].strip()
            correct_choice_letter = correct_full_text[0]

            selected_choice_var = tk.StringVar(value="")
            self.selected_answer_vars.append((selected_choice_var, correct_choice_letter))

            tk.Label(
                question_container, text=question_text, font=("Arial", 12, "bold"),
                anchor='w', justify='left'
            ).pack(fill='x', padx=10, pady=(10, 0))

            radio_buttons_for_question = []

            for choice_text in choices_list:
                choice_letter = choice_text[0]
                radio_button = tk.Radiobutton(
                    question_container,
                    text=choice_text,
                    variable=selected_choice_var,
                    value=choice_letter,
                    anchor='w', justify='left'
                )

                radio_button.pack(fill='x', padx=20, anchor='w')
                radio_buttons_for_question.append((radio_button, choice_text, choice_letter))

            self.radio_button_groups.append((radio_buttons_for_question, correct_choice_letter))

        submit_button = tk.Button(question_container, text="Submit Answers", command=lambda: self.submit_quiz(submit_button))
        submit_button.pack(pady=10)

        window.mainloop()

    def submit_quiz(self, submit_button):
        for (selected_var, correct_letter), (button_group, _) in zip(self.selected_answer_vars, self.radio_button_groups):
            user_selected_letter = selected_var.get()

            for radio_button, original_text, choice_letter in button_group:
                if choice_letter == correct_letter:
                    radio_button.config(fg="green")
                elif choice_letter == user_selected_letter:
                    radio_button.config(fg="red")

        submit_button.config(state='disabled')
