# LEVEL 3 PYTHON GUI QUIZ
# --------------------------------------------------------------
# A general knowledge quiz using basic Python and Tkinter.
# Features:
# - Random questions
# - Score
# - Lives
# - Timer
# - Streak
# - Difficulty
# - Progress bar
# - Restart button
# --------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import random


# ------- Quiz questions -------
questions = [
    {
        "text": "What is the capital city of France?",
        "options": ["Paris", "Madrid", "Rome", "Berlin"],
        "answer": "Paris",
        "difficulty": "Easy"
    },
    {
        "text": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Mercury"],
        "answer": "Mars",
        "difficulty": "Easy"
    },
    {
        "text": "How many continents are there in the world?",
        "options": ["5", "6", "7", "8"],
        "answer": "7",
        "difficulty": "Easy"
    },
    {
        "text": "What is the largest ocean on Earth?",
        "options": [
            "Atlantic Ocean",
            "Indian Ocean",
            "Pacific Ocean",
            "Arctic Ocean"
        ],
        "answer": "Pacific Ocean",
        "difficulty": "Easy"
    },
    {
        "text": "Which animal is the largest mammal in the world?",
        "options": [
            "Elephant",
            "Giraffe",
            "Blue Whale",
            "Hippopotamus"
        ],
        "answer": "Blue Whale",
        "difficulty": "Easy"
    },
    {
        "text": "What gas do humans need to breathe?",
        "options": [
            "Carbon dioxide",
            "Oxygen",
            "Hydrogen",
            "Nitrogen"
        ],
        "answer": "Oxygen",
        "difficulty": "Easy"
    },
    {
        "text": "What is the currency of Japan?",
        "options": ["Yuan", "Won", "Yen", "Dollar"],
        "answer": "Yen",
        "difficulty": "Medium"
    },
    {
        "text": "Who painted the Mona Lisa?",
        "options": [
            "Vincent van Gogh",
            "Leonardo da Vinci",
            "Pablo Picasso",
            "Michelangelo"
        ],
        "answer": "Leonardo da Vinci",
        "difficulty": "Medium"
    },
    {
        "text": "What is the largest planet in our Solar System?",
        "options": [
            "Earth",
            "Saturn",
            "Jupiter",
            "Neptune"
        ],
        "answer": "Jupiter",
        "difficulty": "Medium"
    },
    {
        "text": "Which organ pumps blood around the human body?",
        "options": [
            "Brain",
            "Lungs",
            "Heart",
            "Liver"
        ],
        "answer": "Heart",
        "difficulty": "Medium"
    },
    {
        "text": "Which country is famous for the pyramids of Giza?",
        "options": [
            "Egypt",
            "Greece",
            "Mexico",
            "Italy"
        ],
        "answer": "Egypt",
        "difficulty": "Medium"
    },
    {
        "text": "How many players are on the field for one soccer team?",
        "options": ["9", "10", "11", "12"],
        "answer": "11",
        "difficulty": "Medium"
    },
    {
        "text": "What is the hardest natural substance on Earth?",
        "options": [
            "Gold",
            "Iron",
            "Diamond",
            "Quartz"
        ],
        "answer": "Diamond",
        "difficulty": "Medium"
    },
    {
        "text": "Who was the first person to walk on the Moon?",
        "options": [
            "Buzz Aldrin",
            "Neil Armstrong",
            "Yuri Gagarin",
            "Michael Collins"
        ],
        "answer": "Neil Armstrong",
        "difficulty": "Hard"
    },
    {
        "text": "What is the smallest country in the world?",
        "options": [
            "Monaco",
            "Vatican City",
            "Malta",
            "Liechtenstein"
        ],
        "answer": "Vatican City",
        "difficulty": "Hard"
    }
]


# ------- Game variables -------
current_index = 0
score = 0
lives = 3
streak = 0
time_left = 15
game_running = False


# Shuffle questions so the game is different each time
random.shuffle(questions)


# ------- Create main window -------
root = tk.Tk()
root.title("General Knowledge Quiz")
root.geometry("600x520")
root.resizable(False, False)


# ------- Main frame -------
main = ttk.Frame(root, padding=16)
main.pack(fill="both", expand=True)


# ------- Title -------
title_label = ttk.Label(
    main,
    text="🌍 GENERAL KNOWLEDGE QUIZ",
    font=("Segoe UI", 20, "bold")
)
title_label.pack(pady=(0, 10))


# ------- Game information -------
info_label = ttk.Label(
    main,
    text=""
)
info_label.pack()


# ------- Timer -------
timer_label = ttk.Label(
    main,
    text="Time: 15",
    font=("Segoe UI", 12, "bold")
)
timer_label.pack(pady=5)


# ------- Progress -------
progress_label = ttk.Label(
    main,
    text=""
)
progress_label.pack()


progress_bar = ttk.Progressbar(
    main,
    length=500,
    maximum=len(questions),
    value=0
)
progress_bar.pack(pady=8)


# ------- Question -------
question_label = ttk.Label(
    main,
    text="",
    wraplength=520,
    justify="center",
    font=("Segoe UI", 13, "bold")
)
question_label.pack(pady=15)


# ------- Difficulty -------
difficulty_label = ttk.Label(
    main,
    text=""
)
difficulty_label.pack()


# ------- Answer area -------
selected_answer = tk.StringVar(value="")

options_frame = ttk.Frame(main)
options_frame.pack(fill="x", pady=10)

option_buttons = []


# ------- Feedback -------
feedback_label = ttk.Label(
    main,
    text="",
    font=("Segoe UI", 11, "bold")
)
feedback_label.pack(pady=5)


# ------- Buttons -------
buttons = ttk.Frame(main)
buttons.pack(pady=10)


submit_btn = ttk.Button(
    buttons,
    text="Submit"
)
submit_btn.pack(side="left", padx=5)


next_btn = ttk.Button(
    buttons,
    text="Next",
    state="disabled"
)
next_btn.pack(side="left", padx=5)


restart_btn = ttk.Button(
    buttons,
    text="Restart"
)
restart_btn.pack(side="left", padx=5)


quit_btn = ttk.Button(
    buttons,
    text="Quit",
    command=root.destroy
)
quit_btn.pack(side="left", padx=5)


# ------- Update game information -------
def update_info():
    """Update the score, lives and streak."""

    hearts = "❤️" * lives

    info_label.config(
        text=f"Score: {score}    Lives: {hearts}    Streak: {streak}"
    )


# ------- Clear old answer buttons -------
def clear_options():
    """Remove the old answer buttons."""

    for button in option_buttons:
        button.destroy()

    option_buttons.clear()


# ------- Load question -------
def load_question():
    """Display the current question."""

    global time_left
    global game_running

    if current_index >= len(questions):
        finish_quiz()
        return

    time_left = 15
    game_running = True

    selected_answer.set("")
    feedback_label.config(text="")

    submit_btn.config(state="normal")
    next_btn.config(state="disabled")

    q = questions[current_index]

    # Display question
    question_label.config(
        text=f"Q{current_index + 1}: {q['text']}"
    )

    # Display difficulty
    difficulty_label.config(
        text=f"Difficulty: {q['difficulty']}"
    )

    # Display progress
    progress_label.config(
        text=f"Question {current_index + 1} of {len(questions)}"
    )

    progress_bar["value"] = current_index

    # Remove previous options
    clear_options()

    # Create new answer buttons
    for option in q["options"]:

        rb = ttk.Radiobutton(
            options_frame,
            text=option,
            value=option,
            variable=selected_answer
        )

        rb.pack(anchor="w", pady=3)

        option_buttons.append(rb)

    update_info()
    update_timer()


# ------- Timer -------
def update_timer():
    """Count down the timer."""

    global time_left

    if not game_running:
        return

    timer_label.config(
        text=f"Time: {time_left}"
    )

    if time_left > 0:

        time_left -= 1

        root.after(1000, update_timer)

    else:

        time_out()


# ------- Time runs out -------
def time_out():
    """Remove a life when the timer reaches zero."""

    global lives
    global streak
    global game_running

    if not game_running:
        return

    game_running = False

    lives -= 1
    streak = 0

    feedback_label.config(
        text="⏰ Time's up!",
        foreground="red"
    )

    submit_btn.config(state="disabled")
    next_btn.config(state="normal")

    update_info()

    if lives <= 0:
        game_over()


# ------- Submit answer -------
def submit_answer():
    """Check the answer and update the score."""

    global score
    global lives
    global streak
    global game_running

    choice = selected_answer.get()

    # Make sure the player selected an answer
    if choice == "":
        messagebox.showinfo(
            "Select an answer",
            "Please select one answer before submitting."
        )
        return

    game_running = False

    correct = questions[current_index]["answer"]

    if choice == correct:

        streak += 1

        # Streak gives bonus points
        points = 10 + (streak * 2)

        score += points

        feedback_label.config(
            text=f"✅ Correct! +{points} points",
            foreground="green"
        )

    else:

        lives -= 1
        streak = 0

        feedback_label.config(
            text=f"❌ Incorrect! Correct answer: {correct}",
            foreground="red"
        )

    submit_btn.config(state="disabled")
    next_btn.config(state="normal")

    update_info()

    if lives <= 0:
        game_over()


# ------- Next question -------
def next_question():
    """Move to the next question."""

    global current_index

    if lives <= 0:
        game_over()
        return

    current_index += 1

    if current_index < len(questions):
        load_question()
    else:
        finish_quiz()


# ------- Game over -------
def game_over():
    """End the game when the player loses all lives."""

    global game_running

    game_running = False

    again = messagebox.askyesno(
        "Game Over",
        f"Game Over!\n\n"
        f"Final Score: {score}\n\n"
        f"Play again?"
    )

    if again:
        restart_quiz()
    else:
        root.destroy()


# ------- Finish quiz -------
def finish_quiz():
    """Show the player's final score."""

    global game_running

    game_running = False

    percent = int(
        (score / (len(questions) * 30)) * 100
    )

    if percent > 100:
        percent = 100

    again = messagebox.askyesno(
        "Quiz Complete",
        f"🎉 Quiz Complete!\n\n"
        f"Score: {score}\n"
        f"Percentage: {percent}%\n\n"
        f"Play again?"
    )

    if again:
        restart_quiz()
    else:
        root.destroy()


# ------- Restart quiz -------
def restart_quiz():
    """Reset the game and start again."""

    global current_index
    global score
    global lives
    global streak
    global time_left
    global game_running

    current_index = 0
    score = 0
    lives = 3
    streak = 0
    time_left = 15
    game_running = True

    random.shuffle(questions)

    load_question()


# ------- Connect buttons to functions -------
submit_btn.config(
    command=submit_answer
)

next_btn.config(
    command=next_question
)

restart_btn.config(
    command=restart_quiz
)


# ------- Start the quiz -------
load_question()


# ------- Start the program -------
root.mainloop()