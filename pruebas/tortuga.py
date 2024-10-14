from turtle import Screen, Turtle

IMAGE = "mouse.gif"

def change(x, y):
    turtle.shape(IMAGE)

screen = Screen()
screen.register_shape(IMAGE)

turtle = Turtle('turtle')

screen.onclick(change)
screen.mainloop()