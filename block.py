# block.py
from turtle import Turtle

class Block(Turtle):

    def __init__(self, position, color, points):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the size for block appearance
        self.points = points

    def break_block(self):
        self.hideturtle()  # Hide the block to prevent visual inconsistencies
