 # Simple Pong in Python 3
import turtle          # base package
import winsound        # base package
from tkinter import *  # base package
from window import gui_name

# Input names
root = Tk()
my_gui = gui_name(root)
root.mainloop()
print("Names retrieved were", my_gui.players)
player_names = [str(my_gui.players[0]) + ": 0", str(my_gui.players[1]) + ": 0"]
player_names_update = [str(my_gui.players[0]) + ": {}", str(my_gui.players[1]) + ": {}"]
player_names = ' '.join(player_names)
player_names_update = ' '.join(player_names_update)

# Main window screen
wn = turtle.Screen()
wn.title("Pong by @Chris")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # stops window from updating

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # sets speed to maximum possible speed
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # default is 20px by 20px, so now 100px by 20px
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # sets speed to maximum possible speed
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # default is 20px by 20px, so now 100px by 20px
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # sets speed to maximum possible speed; animation speed
ball.shape("circle")
ball.color('white')
ball.shapesize(stretch_wid=2, stretch_len=2)  # default is 20px by 20px, so now 100px by 20px
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25  # everytime ball moves, it moves by 0.5 pixels
ball.dy = 0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(player_names, align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()  # paddle_a is name of object we defined above; .ycor() is from turtle module and return ycor
    y += 20  # add 20 pixels to y coordinate
    paddle_a.sety(y)  # set new coordinate of y to paddle_a


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # paddle_a is name of object we defined above; .ycor() is from turtle module and return ycor
    y += 20  # add 20 pixels to y coordinate
    paddle_b.sety(y)  # set new coordinate of y to paddle_a


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")  # when user presses "w", call function paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()  # every time loop runs it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # every loop it moves ball_dx pixels, with first loop starting at center
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:  # 600 height window, split difference, minus half the ball height, which is 20 pixels
        ball.sety(290) # housekeeping to prevent errors
        ball.dy *= -1  # reverses direction, keeping ball.dx the same as above
        winsound.PlaySound("wallbounce.wav", winsound.SND_ASYNC) # sound when ball hits wall and synchronize properly

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("wallbounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:  # 800 width window, split difference, minus half the ball height, which is 20 pixels
        ball.goto(0, 0) # ball goes back to center
        ball.dx *= -1
        score_a += 1
        pen.clear() # remove previous pen
        pen.write(player_names_update.format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("wallbounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:  # 800 width window, split difference, minus half the ball height, which is 20 pixels
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()  # remove previous pen
        pen.write(player_names_update.format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("wallbounce.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60): # ball touches paddle xaxis and ball touches paddle yaxis + a bit extra because of ball size on both ends
        ball.setx(340)  # move ball to 340 if ball falls between 340 and 350
        ball.dx *= -1
        winsound.PlaySound("wallbounce.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60):  # ball touches paddle xaxis and ball touches paddle yaxis + a bit extra because of ball size on both ends
        ball.setx(-340)
        ball.dx *= - 1
        winsound.PlaySound("wallbounce.wav", winsound.SND_ASYNC)
