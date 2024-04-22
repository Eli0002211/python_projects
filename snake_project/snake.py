from turtle import Turtle  # import from the turtle module

# set the starting positions as a constant

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:  # define the snake class

    def __init__(self):

        self.segments = []  # create a list of segments

        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")  # create a new segment in a square shape

            new_segment.color("white")  # set the colour

            new_segment.penup()  # set the pen as up to prevent drawing on the screen

            new_segment.goto(position)  # tell the segment to go to its position

            self.segments.append(new_segment)  # add the segment to the list

    def move(self):  # define the move function

        for seg_num in range(len(self.segments) - 1, 0,
                             -1):  # each segment will move forward, starting from the last one

            new_x = self.segments[
                seg_num - 1].xcor()  # segment will move to the current position of the one in front of it in the list

            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(15)  # move the head forward on it's own

    def create_new_segment(self):  # define the function to create a new segment

        new_x = self.segments[-1].xcor()  # Use the x-coordinate of the last segment

        new_y = self.segments[-1].ycor()  # Use the y-coordinate of the last segment

        new_segment = Turtle("square")  # set shape as square

        new_segment.color("white")  # set colour

        new_segment.penup()  # bring the pen up to avoid drawing on screen

        new_segment.goto(new_x, new_y)  # Go to the position of the last segment

        self.segments.append(new_segment)  # add segment to list

    def turn_left(self):  # define function to turn left

        self.segments[0].left(90)

    def turn_right(self):  # define function to turn right

        self.segments[0].right(90)

