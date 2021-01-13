from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-260, 240)
        self.hideturtle()
        self.update_score()
        # turtle.write(arg, move=False, align="left", font=("Arial", 8, "normal"))

    def update_score(self):
        global LEVEL
        self.clear()
        self.write(f"level:{LEVEL+1} ", move=False, align="left", font=FONT)
        LEVEL = LEVEL + 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align="left", font=FONT)



