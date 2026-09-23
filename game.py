# FOOTBALL JUGGLING GAME
# --------------------------------------------------------------
# A simple football game made with Tkinter.
# The aim is to keep the ball in the air and get a high score.
# --------------------------------------------------------------

# ------- 1. Import tkinter -------
# Tkinter lets us create the game window, buttons and labels.
import tkinter as tk
from tkinter import messagebox


# ------- 2. Game variables -------
# These variables keep track of what is happening in the game.

score = 0
ball_height = 0
game_started = False


# ------- 3. Create the main window -------
# This creates the window that the game will appear in.

root = tk.Tk()
root.title("Football Juggling Game")
root.geometry("500x500")


# ------- 4. Create the title -------
# This displays the name of the game at the top.

title_label = tk.Label(
    root,
    text="⚽ Football Juggling",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=10)


# ------- 5. Create the score label -------
# This shows the player's current score.

score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 16)
)

score_label.pack(pady=5)


# ------- 6. Create the game area -------
# This is the area where the football will be shown.

game_area = tk.Canvas(
    root,
    width=400,
    height=300,
    bg="green"
)

game_area.pack(pady=10)


# ------- 7. Create the football -------
# This creates a simple circle to represent the football.

ball = game_area.create_oval(
    175, 220,
    225, 270,
    fill="white"
)


# ------- 8. Create the ground -------
# This line represents the ground.

ground = game_area.create_line(
    0, 270,
    400, 270,
    fill="white",
    width=5
)


# ------- 9. Juggle function -------
# This function is called when the player presses Juggle.
# It increases the score and moves the ball upwards.

def juggle_ball():

    global score
    global ball_height
    global game_started

    game_started = True

    # Increase the score by 1
    score += 1

    # Update the score on the screen
    score_label.config(text=f"Score: {score}")

    # Move the ball upwards
    game_area.move(ball, 0, -30)

    # Bring the ball back down after a short time
    root.after(300, bring_ball_down)


# ------- 10. Bring the ball down -------
# This moves the football back towards the ground.

def bring_ball_down():

    game_area.move(ball, 0, 30)


# ------- 11. Restart function -------
# This resets the game back to the beginning.

def restart_game():

    global score
    global game_started

    score = 0
    game_started = False

    # Reset the score
    score_label.config(text="Score: 0")

    # Put the ball back in its starting position
    game_area.coords(
        ball,
        175, 220,
        225, 270
    )


# ------- 12. Juggle button -------
# This button calls the juggle_ball function.

juggle_button = tk.Button(
    root,
    text="Juggle ⚽",
    font=("Arial", 14),
    command=juggle_ball
)

juggle_button.pack(pady=5)


# ------- 13. Restart button -------
# This button calls the restart_game function.

restart_button = tk.Button(
    root,
    text="Restart",
    font=("Arial", 12),
    command=restart_game
)

restart_button.pack(pady=5)


# ------- 14. Quit button -------
# This closes the game when clicked.

quit_button = tk.Button(
    root,
    text="Quit",
    font=("Arial", 12),
    command=root.destroy
)

quit_button.pack(pady=5)


# ------- 15. Start the game -------
# mainloop keeps the window open and allows the player
# to interact with the buttons.

root.mainloop()