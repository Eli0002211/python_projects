from turtle import Turtle  # import elements from turtle

# set the alignment and font as constants

ALIGNMENT = "center"

FONT = ("Courier", 16, "normal")


class Score_Counter(Turtle):  # define the score counter class, which inherits from the turtle class

    def __init__(self):
        super().__init__()

        self.counter = 0  # initially set to 0

        with open("high_score.txt") as file: #open the file that contains the high score
            contents = file.read()

        self.high_score = int(contents) #set the high score

        self.hideturtle()  # hide the turtle which prints the score text

        self.teleport(-10, 270)  # teleport to top of screen

        self.pencolor("white")  # set the colour to white

        self.scoreboard = (f"Score: {self.counter}     High Score : {self.high_score}")

        self.write(f"{self.scoreboard}",False,ALIGNMENT,FONT)  # write the score

    def update_score(self): #updates the scoreboard
        self.clear()
        self.scoreboard = (f"Score: {self.counter}     High Score : {self.high_score}")
        self.write(f"{self.scoreboard}",False,ALIGNMENT,FONT)
    def increase_score(self):  # define function to increase the score
        self.counter += 1  # counter is increased by 1
        self.update_score()

    def reset(self): #update the high score file and scoreboard if players score is higher than current highscore
        if self.counter > self.high_score:
            self.high_score = self.counter
            with open("high_score.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.counter = 0
        self.update_score()