# FOOTBALL BRICK BREAKER
# --------------------------------------------------------------
# Move the platform left and right.
# Break all the bricks, then get the ball into the goal.
# Each level gets harder.
# --------------------------------------------------------------

# 1. IMPORTS
import tkinter as tk
import random


# 2. GAME VARIABLES
score = 0
lives = 3
level = 1

ball_dx = 5
ball_dy = -5

game_running = False
goal_open = False

bricks = []
powerups = []


# 3. MAIN WINDOW
root = tk.Tk()
root.title("Football Brick Breaker")
root.geometry("600x700")


# 4. GAME INFORMATION
info = tk.Label(
    root,
    text="Score: 0   Lives: 3   Level: 1",
    font=("Arial", 15, "bold")
)
info.pack(pady=5)


# 5. GAME AREA
canvas = tk.Canvas(
    root,
    width=500,
    height=600,
    bg="darkgreen"
)
canvas.pack()


# 6. PLAYER
player = canvas.create_rectangle(
    210, 540, 290, 560,
    fill="blue"
)


# 7. BALL
ball = canvas.create_oval(
    240, 500, 260, 520,
    fill="white"
)


# 8. GOAL
goal = canvas.create_rectangle(
    200, 570, 300, 600,
    fill="gold"
)

goal_text = canvas.create_text(
    250, 585,
    text="GOAL",
    font=("Arial", 14, "bold")
)

canvas.itemconfig(goal, state="hidden")
canvas.itemconfig(goal_text, state="hidden")


# 9. UPDATE SCORE
def update_info():

    info.config(
        text=f"Score: {score}   Lives: {lives}   Level: {level}"
    )


# 10. CREATE BRICKS
def create_bricks():

    bricks.clear()

    rows = min(2 + level, 6)

    for row in range(rows):

        for column in range(7):

            x = 35 + column * 68
            y = 40 + row * 30

            brick = canvas.create_rectangle(
                x, y,
                x + 60, y + 20,
                fill="red"
            )

            bricks.append(brick)


# 11. MOVE PLAYER
def move_player(event):

    position = canvas.coords(player)

    if event.keysym == "Left" and position[0] > 0:
        canvas.move(player, -30, 0)

    if event.keysym == "Right" and position[2] < 500:
        canvas.move(player, 30, 0)


# 12. CHECK BRICKS
def check_bricks():

    global score
    global ball_dy

    ball_position = canvas.coords(ball)

    for brick in bricks[:]:

        brick_position = canvas.coords(brick)

        if (
            ball_position[2] >= brick_position[0]
            and ball_position[0] <= brick_position[2]
            and ball_position[3] >= brick_position[1]
            and ball_position[1] <= brick_position[3]
        ):

            canvas.delete(brick)
            bricks.remove(brick)

            score += 10
            ball_dy = -ball_dy

            # Small chance of a power-up
            if random.randint(1, 5) == 1:
                create_powerup(
                    brick_position[0],
                    brick_position[1]
                )

            break


# 13. POWER-UP
def create_powerup(x, y):

    powerup = canvas.create_oval(
        x, y,
        x + 15, y + 15,
        fill="yellow"
    )

    powerups.append(powerup)


def move_powerups():

    global lives

    player_position = canvas.coords(player)

    for powerup in powerups[:]:

        canvas.move(powerup, 0, 4)

        position = canvas.coords(powerup)

        if (
            position[2] >= player_position[0]
            and position[0] <= player_position[2]
            and position[3] >= player_position[1]
            and position[1] <= player_position[3]
        ):

            canvas.delete(powerup)
            powerups.remove(powerup)

            # Power-up gives an extra life
            lives += 1

        elif position[1] > 600:

            canvas.delete(powerup)
            powerups.remove(powerup)


# 14. OPEN GOAL
def open_goal():

    global goal_open

    goal_open = True

    canvas.itemconfig(goal, state="normal")
    canvas.itemconfig(goal_text, state="normal")


# 15. NEXT LEVEL
def next_level():

    global level
    global goal_open
    global ball_dx
    global ball_dy

    level += 1
    goal_open = False

    canvas.itemconfig(goal, state="hidden")
    canvas.itemconfig(goal_text, state="hidden")

    create_bricks()

    # Make the ball faster each level
    ball_dx = 5 + level
    ball_dy = -(5 + level)

    canvas.coords(ball, 240, 500, 260, 520)
    update_info()


# 16. MOVE BALL
def move_ball():

    global ball_dx
    global ball_dy
    global lives
    global game_running

    if not game_running:
        return

    canvas.move(ball, ball_dx, ball_dy)

    position = canvas.coords(ball)

    # Walls
    if position[0] <= 0 or position[2] >= 500:
        ball_dx = -ball_dx

    if position[1] <= 0:
        ball_dy = -ball_dy

    # Bricks
    check_bricks()

    # Player
    player_position = canvas.coords(player)

    if (
        position[2] >= player_position[0]
        and position[0] <= player_position[2]
        and position[3] >= player_position[1]
        and position[1] <= player_position[3]
        and ball_dy > 0
    ):

        ball_dy = -abs(ball_dy)


    # All bricks destroyed
    if len(bricks) == 0 and not goal_open:
        open_goal()


    # Goal
    if goal_open:

        goal_position = canvas.coords(goal)

        if (
            position[2] >= goal_position[0]
            and position[0] <= goal_position[2]
            and position[3] >= goal_position[1]
            and position[1] <= goal_position[3]
        ):
            next_level()


    # Ball missed
    if position[1] > 600:

        lives -= 1

        if lives <= 0:

            game_running = False
            canvas.create_text(
                250, 300,
                text="GAME OVER",
                fill="white",
                font=("Arial", 30, "bold")
            )

        else:

            canvas.coords(ball, 240, 500, 260, 520)

    move_powerups()
    update_info()

    root.after(20, move_ball)


# 17. START GAME
def start_game():

    global game_running

    game_running = True

    create_bricks()
    move_ball()


# 18. RESTART GAME
def restart_game():

    global score
    global lives
    global level
    global game_running
    global goal_open

    score = 0
    lives = 3
    level = 1
    game_running = True
    goal_open = False

    canvas.delete("all")

    # Recreate player and ball
    global player
    global ball
    global goal
    global goal_text

    player = canvas.create_rectangle(
        210, 540, 290, 560,
        fill="blue"
    )

    ball = canvas.create_oval(
        240, 500, 260, 520,
        fill="white"
    )

    goal = canvas.create_rectangle(
        200, 570, 300, 600,
        fill="gold"
    )

    goal_text = canvas.create_text(
        250, 585,
        text="GOAL",
        font=("Arial", 14, "bold")
    )

    canvas.itemconfig(goal, state="hidden")
    canvas.itemconfig(goal_text, state="hidden")

    create_bricks()
    update_info()
    move_ball()


# 19. BUTTONS
start_button = tk.Button(
    root,
    text="Start",
    command=start_game
)
start_button.pack(side="left", padx=180)

restart_button = tk.Button(
    root,
    text="Restart",
    command=restart_game
)
restart_button.pack()


# 20. CONTROLS
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)


# 21. START
create_bricks()
update_info()

root.mainloop()