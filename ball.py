import random
from turtle import Turtle

BALL_STARTING_DIRECTION = random.choice([225, 135, 45, 315])
TOP = 290
BOTTOM = -290
FIRST_THIRD_QUADRANT = "first or third"
SECOND_FOURTH_QUADRANT = "second or fourth"


class Ball:
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.setheading(BALL_STARTING_DIRECTION)

    def ball_motion(self):
        self.ball.forward(20)

    def ball_angle_quadrant(self):
        current_angle = self.ball.heading()
        if 0 <= current_angle <= 90 or 180 <= current_angle <= 270:
            return "first or third", current_angle - 90, current_angle + 90
        elif 90 <= current_angle <= 180 or 270 <= current_angle <= 360:
            return "second or fourth", current_angle + 90, current_angle - 90

    def wall_collision(self):
        self.ball.speed("fastest")
        current_angle = self.ball_angle_quadrant()
        if not (self.ball.ycor() >= TOP or self.ball.ycor() <= BOTTOM):
            return None
        else:
            self.ball.setheading(current_angle[1])
        self.ball.speed("normal")

    def paddle_collision(self, paddle):
        self.ball.speed("fastest")
        current_angle = self.ball_angle_quadrant()
        if self.ball.distance(paddle.position()) > 25:
            return False
        else:
            self.ball.setheading(current_angle[2])
            return True
