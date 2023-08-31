"""gets a number, then guesses randomly, then the guessing area gets narrower to finally find the answer."""

from turtle import Turtle, Screen
import random


"""initials"""
high = 501
mini = 0
maxi = 500
num = -1
new_maxi = maxi
new_mini = mini

"""screen making."""
screen = Screen()
screen.setup(1000, high + 40)

"""prompt to get the number."""
while not (0 <= num <= 500):
    num = int(screen.textinput("Guessing Game", "Say a number between 0 and 500: "))

"""a list of numbers from 0 to 'hi'"""
num_list = []
for n in range(high):
    num_list.append(n)

"""a list of weights for random.choices"""
weight_list = []
for _ in range(high):
    weight_list.append(0)

"""graph stuff"""
"""the line that shows the chosen number"""
num_line = Turtle()
num_line.hideturtle()
num_line.color("green")
num_line.penup()
num_line.setposition(- 480, - 250 + num)
num_line.pendown()
num_line.goto(+ 480, - 250 + num)
num_line.penup()
num_line.speed(0)

"""the dot that shows the guess"""
guess_dot = Turtle()
guess_dot.hideturtle()
guess_dot.pencolor("black")
guess_dot.penup()
guess_dot.speed(0)

"""max and min of the guess area"""
max_line = Turtle()
max_line.hideturtle()
max_line.color("red")
min_line = Turtle()
min_line.hideturtle()
min_line.color("blue")
max_line.penup()
min_line.penup()
max_line.setposition(- 480, - 250 + maxi)
min_line.setposition(- 480, - 250 + mini)
max_line.pendown()
min_line.pendown()
max_line.speed(0)
min_line.speed(0)

""" the main loop that continues until finding the number or running out of screen length. """
guess = -1
guess_try = 0
while guess != num and guess_try * 2 < 960:
    random_guess = random.randint(mini, maxi)
    # print(f"random_guess: {random_guess}")

    """because the weight list should not be all 0."""
    if random_guess == 0:
        weight_list[0] = 1
    else:
        """making the weight list centered around the random_guess"""

        """first from 0 to random_guess,"""
        for i in range(0, random_guess):
            weight_list[i] = i ** 10

        """then from random_guess + 1 to end of the list."""
        for j in range(0, high - random_guess):

            """for it to not to turn negative weights"""
            if random_guess - j >= 0:
                weight_list[random_guess + j] = (random_guess - j) ** 10
            else:
                weight_list[random_guess + j] = 0

    """random.choices returns a list, in this case 1 member only."""
    guess_list = random.choices(num_list, weight_list, k=1)
    guess = guess_list[0]
    # print(f"guess: {guess}")

    """drawing the dot for the guess."""
    guess_dot.setposition(- 480 + guess_try * 2, - 250 + guess)
    guess_dot.dot(3)

    """qualifying the guess."""
    if guess == num:
        # print(f"Number found: {guess}")
        guess_dot.dot(5)
        break

    """new maxi and mini making snd qualification. acts in a way that the lines get closer."""
    for s in reversed(range(1, high)):
        if abs(guess - num) <= s:
            new_maxi = random_guess + s
            new_mini = random_guess - s

    if new_maxi < maxi and maxi - new_maxi < 500:
        maxi = new_maxi
    elif new_maxi > maxi and new_maxi - maxi < 300:
        maxi = new_maxi

    if new_mini > mini and new_mini - mini < 500:
        mini = new_mini
    elif new_mini < mini and mini - new_mini < 300:
        mini = new_mini

    # maxi = new_maxi
    # mini = new_mini

    if maxi > high - 1:
        maxi = high - 1
    if mini < 0:
        mini = 0

    # if maxi == mini:
    #     if maxi == num:
    #         break
    #     else:
    #         maxi += 1
    #         mini -= 1
    # if mini > maxi:
    #     l = mini
    #     mini = maxi
    #     maxi = l
    # print(f"maxi: {maxi}")
    # print(f"mini: {mini}")

    """drawing the max and min lines."""
    max_line.setposition(- 480 + guess_try * 2, - 250 + maxi)
    min_line.setposition(- 480 + guess_try * 2, - 250 + mini)

    """keeps count of the number of guesses."""
    guess_try += 1

print(f"guess_try {guess_try}")

screen.exitonclick()
