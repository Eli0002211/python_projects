from turtle import Turtle  # import from the turtle module

from random import Random, randint  # import from the random module


class Food(Turtle):  # define the food class, which inherits from the turtle class

    def __init__(self):
        super().__init__()

        self.shape("circle")  # set shape as a circle

        self.shapesize(0.7)  # set the size of the food

        self.color("blue")  # set the colour

        self.penup()  # bring the pen up to prevent lines being drawn

        self.speed("fastest")  # set the speed to fastest to prevent the movements being shown

        self.goto(randint(-280, 280),
                  randint(-280, 280))  # send the first piece of food to appear in a random location within the screen