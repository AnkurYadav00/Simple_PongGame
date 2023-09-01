"""
PROBLEM BREAKDOWN:

1. build the paddle and ball
2. set the starting position of ball and paddles
3. control the paddle
4. make ball bounce from wall from top and bottom and paddles
5. create scoreboard
6. divide screen into two regions


1. create the screen
2. create and move the paddle
3. create another paddle
4. create the ball and make it move
5. detect collision with the wall and bounce
6. detect collision with the paddle and bounce
7. detect when misses paddle
8. score

"""
import time
from turtle import Screen

from Paddle import Paddles
from ScoreBoard import Score
from ball import Ball


def main():
    screen = Screen()
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.setup(1000, 600)
    screen.tracer(0)

    screen.listen()

    # create paddle and ball object
    paddle = Paddles()
    ball = Ball()
    score = Score()
    screen.update()

    # control paddles motion
    screen.onkeypress(paddle.right_paddle_moveDown, "Down")
    screen.onkeypress(paddle.right_paddle_moveUp, "Up")
    screen.onkeypress(paddle.left_paddle_moveDown, "s")
    screen.onkeypress(paddle.left_paddle_moveUp, "w")

    is_game_on = True

    while is_game_on:
        screen.update()
        time.sleep(0.05)
        for i in paddle.left_paddle:
            if ball.paddle_collision(i):
                score.left_scored()
                break
        for i in paddle.right_paddle:
            if ball.paddle_collision(i):
                score.right_scored()
                break

        ball.wall_collision()
        ball.ball_motion()

        if ball.ball.xcor() > 500 or ball.ball.xcor() < -500:
            is_game_on = not is_game_on
            score.gameOver()

    screen.exitonclick()


if __name__ == "__main__":
    main()
