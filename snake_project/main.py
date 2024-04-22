
from score_counter import Score_Counter, FONT, ALIGNMENT  # import elements from score counter
from turtle import Screen  # import elements from turtle
screen = Screen()  # create the screen
score_counter = Score_Counter()  # initialise the score counter

screen.setup(600, 600)  # set the width and height

screen.bgcolor("black")  # set the background to black

screen.title("Snake")  # set the title to say Snake

screen.tracer(0)  # turn off tracer to prevent the snake segments from moving with a 'caterpillar' effect
def snake_game():  # game is held inside a function to allow for easy recursion

    from turtle import Screen  # import elements from turtle

    from time import sleep  # import elements from time

    from snake import Snake, STARTING_POSITIONS  # import elements from snake

    from food import Food  # import elements from food


    from random import randint  # import elements from random

    screen.bgcolor("black")  # set the background to black

    screen.title("Snake")  # set the title to say Snake

    score_counter.update_score() #update the score

    screen.tracer(0)  # turn off tracer to prevent the snake segments from moving with a 'caterpillar' effect

    food = Food()  # initialise food

    snake = Snake()  # initialise the snake

    # Set up key bindings

    screen.onkey(fun=snake.turn_left, key="Left")

    screen.onkey(fun=snake.turn_right, key="Right")

    screen.listen()  # listen for inputs

    # set the sleep timer, which determines how long the screen waits to update itself, which controls the speed the snake appears to move at.

    sleep_timer = 0.2

    # set the game counter, which will change if a game over occurs and break the while loop to stop the snake from moving.

    game_counter = 0

    while game_counter == 0:  # create the rest of the script within the while loop.

        screen.update()  # update the screen while the game is active

        sleep(sleep_timer)  # the sleep timer will be activated to make the snakes movements run more smoothly

        snake.move()  # the snake will continuously move forward

        if snake.segments[0].distance(food) < 20:  # detect when the snake head has collided with the food

            sleep_timer *= 0.9  # decrease the sleep timer, which will increase the perceived speed of the snake

            score_counter.clear()  # clear the current score counter off the screen

            score_counter.increase_score()  # replace with the new score counter showing an increased count

            food.goto(randint(-280, 280), randint(-280, 280))  # food will move to a random location on screen

            snake.create_new_segment()  # add a new segment to the snake

        # detect collision with the walls

        if snake.segments[0].xcor() > 300 or snake.segments[0].ycor() > 300 or snake.segments[0].xcor() < -300 or \
                snake.segments[0].ycor() < -300:

            score_counter.reset()  # initiate game over

            repeat = screen.textinput(title="Game Over",
                                      prompt="Play again?[Y/N]").upper()  # create a pop up to ask if user wants to play again

            game_counter += 1  # edit the game counter, which breaks the while loop and stops the snake from moving

            if repeat == "Y":  # if player chose "Y", the game function is called, looping the script
                screen.clear()  # clear any previous outputs
                screen.update()
                snake_game()

        # cause a game over if the snake collides with itself

        for segment in snake.segments[1:]:

            if snake.segments[0].distance(segment) < 5:

                score_counter.reset()  # incur all the same game over procedures as the previous if loop

                repeat = screen.textinput(title="Game Over", prompt="Play again?[Y/N]").upper()
                game_counter += 1 #update the game counter
                if repeat == "Y":
                    screen.clear()  # clear any previous outputs
                    screen.update()
                    snake_game()

    screen.exitonclick()  # don't exit the screen until clicked on


snake_game()  # call the inital game function