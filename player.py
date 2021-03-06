from turtle import Turtle

STARTING_POSITIONS = (0, -270)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        # self.shapesize(stretch_wid=2, stretch_len=0.5)
        self.color('black')
        self.setheading(90)
        self.go_to_start()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITIONS)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
