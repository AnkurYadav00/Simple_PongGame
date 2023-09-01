from turtle import Turtle

RIGHT_PADDLE_POSITION = [(480, 20), (480, 0), (480, -20)]
LEFT_PADDLE_POSITION = [(-490, 20), (-490, 0), (-490, -20)]
PADDLE_CONSTRAINT = 290


class Paddles:
    def __init__(self):
        self.segment = None
        self.right_paddle = []
        self.left_paddle = []
        self.create_left_paddle()
        self.create_right_paddle()

    def create_right_paddle(self):
        for i in range(3):
            self.right_paddle.append(self.create_paddle(RIGHT_PADDLE_POSITION[i]))

    def create_left_paddle(self, ):
        for i in range(3):
            self.left_paddle.append(self.create_paddle(LEFT_PADDLE_POSITION[i]))

    def create_paddle(self, position):
        self.segment = Turtle()
        self.segment.speed("fastest")
        self.segment.penup()
        self.segment.shape("square")
        self.segment.color("white")
        self.segment.goto(position)
        self.segment.setheading(90)
        return self.segment

    def left_paddle_moveUp(self):
        if self.left_paddle[0].ycor() >= PADDLE_CONSTRAINT:
            return None
        for i in range(len(self.left_paddle)):
            self.left_paddle[i].forward(20)

    def right_paddle_moveUp(self):
        if self.right_paddle[0].ycor() >= PADDLE_CONSTRAINT:
            return None
        for i in range(len(self.right_paddle)):
            self.right_paddle[i].forward(20)

    def left_paddle_moveDown(self):
        if self.left_paddle[-1].ycor() <= -PADDLE_CONSTRAINT:
            return None
        for i in range(len(self.left_paddle) - 1, -1, -1):
            self.left_paddle[i].backward(20)

    def right_paddle_moveDown(self):
        if self.right_paddle[-1].ycor() <= -PADDLE_CONSTRAINT:
            return None
        for i in range(len(self.right_paddle) - 1, -1, -1):
            self.right_paddle[i].backward(20)
