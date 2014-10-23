#Matt Koppelman
#GIS 501
#Lab 3 Problem 4



import turtle

turtle.title("Tommy the Turtle - Shape Drawer")
turtle.shape("turtle")
turtle.color("green")
turtle.pencolor("green")

print "Welcome to Tommy the Turtle's Shape Drawer."  

sides = int(input("Please enter the number of sides for your shape: "))
length = 600 / sides
angle = 360 / sides

if sides < 3:
	print "Please start over."
elif sides >= 3:
	for side in range(sides):
		turtle.forward(length)
		turtle.left(angle)
		
print "Click to say goodbye to Tommy"
	

turtle.exitonclick()