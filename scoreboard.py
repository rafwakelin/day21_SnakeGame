from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
POSITION = (0, 270)


class Scoreboard(Turtle):
    """Creates a score board"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(POSITION)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def new_score(self):
        """Once the snake eats food changes the score and displays the new value"""
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Write Game Over in the center of the screen"""
        self.color("white")
        self.goto(0, 0)
        self.write(arg="Game Over".upper(), align="center", font=("Courier", 40, "normal"))
