import turtle


def main():
    turtle1 = turtle.Turtle()
    turtle.speed(0)
    # for i in range(30):
    # turtle1.right(10)
    # turtle1.forward(5)
    # for n in range(4):
    # turtle1.forward(50)
    # turtle1.right(90)

    # for i in range(30):
    # turtle1.forward(i*15)
    # turtle1.right(144)
    # turtle1.pencolor("#32D486")
    # for i in range(40):
    # turtle1.forward(150)
    # turtle1.left(123) # Let's go counterclockwise this time

    turtle1.pencolor("#D6305F")
    # for i in range(40):
    # turtle1.forward(300)
    # # turtle1.left(123)
    # num_sides = 6
    # side_length = 170
    # angle = 360.0 / num_sides

    # for i in range(num_sides):
    # turtle1.forward(side_length)
    # turtle1.right(angle)

    dot_interval = 25
    dot_distance = 35
    width = 5
    height = 7

    turtle1.penup()

    for y in range(height):
        for i in range(width):
            turtle1.forward(dot_interval)
            turtle1.dot()
        turtle1.backward(dot_interval * width)
        turtle1.right(90)
        turtle1.forward(dot_distance)
        turtle1.left(90)
    # turtle.done()#turtle.Screen().mainloop() and turtle.done() are variants of turtle.mainloop()
    turtle.exitonclick()  # aka turtle.Screen().exitonclick() binds the screen click event to do a turtle.bye() and then invokes turtle.mainloop()


if __name__ == '__main__':
    main()
