import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)


def square(length, angle):
	for i in range(4):
		my_turtle.forward(length)#Attantion!!!! TAB!!!
		my_turtle.right(angle)
	
for i in range(160) :
	print (square(100, 90))
	my_turtle.left(11)
#Вопрос- какие еще функции имеются у черепахи и где их искать?