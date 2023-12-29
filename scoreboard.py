from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = self.get_high_score()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=330)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   high score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align=ALIGNMENT,
                   font=FONT)
        self.print_final_score()

    def print_final_score(self):
        self.goto(0, 50)
        self.write(arg=f"Your final Score is : {self.score}", align=ALIGNMENT, font=FONT)

    @staticmethod
    def get_high_score():
        try:
            with open("high_score.txt", mode="r") as file:
                content = file.read()

        except FileNotFoundError:
            with open("high_score.txt", mode="w") as file:
                file.write("0")

            with open("high_score.txt", mode="r") as file:
                content = file.read()

        return int(content)
