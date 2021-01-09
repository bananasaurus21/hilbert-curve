import turtle

# Defining the recursive function
def hilbert(turtle, level, angle, step): 

	if level == 0: 
		return

	turtle.right(angle) 
	hilbert(turtle, level-1, -angle, step) 

	turtle.forward(step) 
	turtle.left(angle) 
	hilbert(turtle, level-1, angle, step) 

	turtle.forward(step) 
	hilbert(turtle, level-1, angle, step) 

	turtle.left(angle) 
	turtle.forward(step) 
	hilbert(turtle, level-1, -angle, step) 
	turtle.right(angle) 

# Test parameters
level = int(input('Enter desired level of Hilbert curve: '))
angle = 90
step = 30

# Creating turtle object 
t = turtle.Turtle()
t.color('violet')
t.pensize(3)
t.screen.bgcolor('black')

# Calling the function
hilbert(t, level, angle, step)	 
