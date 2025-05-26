import tkinter as tk

def load_questions_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    questions_data = []
    for index in range(0, len(lines), 6):
        if lines[index].startswith("Q") and lines[index + 5].startswith("Correct answer:"):
            question_text = lines[index]
            choices = lines[index + 1 : index + 5]
            correct_answer_line = lines[index + 5]
            questions_data.append((question_text, choices, correct_answer_line))
    return questions_data

def display_quiz_window(questions_data):
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

    selected_answer_vars = []
    radio_button_groups = []

    for question_index, (question_text, choices_list, correct_answer_line) in enumerate(questions_data):
        correct_full_text = correct_answer_line.split(":", 1)[1].strip()
        correct_choice_letter = correct_full_text[0]

        selected_choice_var = tk.StringVar(value="")
        selected_answer_vars.append((selected_choice_var, correct_choice_letter))

        tk.Label(
            question_container, text=question_text, font=("Arial", 12, "bold"),
            anchor='w', justify='left'
        ).pack(fill='x', padx=10, pady=(10, 0))

        radio_buttons_for_question = []

        for choice_text in choices_list:
            choice_letter = choice_text[0]  # 'a', 'b', etc.
            radio_button = tk.Radiobutton(
                question_container,
                text=choice_text,
                variable=selected_choice_var,
                value=choice_letter,
                anchor='w', justify='left'
            )

            radio_button.pack(fill='x', padx=20, anchor='w')
            radio_buttons_for_question.append((radio_button, choice_text, choice_letter))

        radio_button_groups.append((radio_buttons_for_question, correct_choice_letter))

    def submit_quiz():
        for (selected_var, correct_letter), (button_group, correct_choice_letter) in zip(selected_answer_vars, radio_button_groups):
            user_selected_letter = selected_var.get()

            for radio_button, original_text, choice_letter in button_group:
                display_text = original_text

                if choice_letter == correct_choice_letter:
                    display_text += " *"
                    radio_button.config(fg="green")
                elif choice_letter == user_selected_letter:
                    radio_button.config(fg="red")

        submit_button.config(state='disabled')

    submit_button = tk.Button(question_container, text="Submit Answers", command=submit_quiz)
    submit_button.pack(pady=10)

    window.mainloop()

file_path = 'quiz.txt'
quiz_questions = load_questions_from_file(file_path)
display_quiz_window(quiz_questions)
