import turtle
import random
screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('red')
t = turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t2.hideturtle()
t3.hideturtle()


#First Slide
t.penup()
t.goto(0, 200)
t.pendown()
t.write('Hello', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 150)
t.pendown()
t.write('My name is Chris Kozar', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, -50)
t.pendown()
t.write('This is my Presenation', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor('Blue')
t.fillcolor('Blue')
t.begin_fill()
t.goto(100, 0)
t.goto(50, 100)
t.goto(0, 0)
t.end_fill()

t.penup()
t.goto(100, -200)
t.pendown()
screen.addshape('Kemba Walker.gif')
t.shape('Kemba Walker.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(-100, -200)
t.pendown()
screen.addshape('KembaWalker2.gif')
t.shape('KembaWalker2.gif')
t.stamp()
t.shape('classic')





#Second Slide
round = input("Press Enter to Continue: ")
t.clear()
screen.bgcolor('dodgerblue')
t.penup()
t.goto(0, 200)
t.pendown()
t.write('My Favorite Foods', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 150)
t.pendown()
t.write('1. Chicken Sandwich', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 100)
t.pendown()
t.write('2. Chinese Food', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 50)
t.pendown()
t.write('3. Pizza', font=("ariel", 30, "italic"), align="center")

t.setheading(45)
t.penup()
t.goto(0,-85)
t.pendown()
t.pencolor("cyan")
t.fillcolor("cyan")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.goto(100, -200)
t.pendown()
screen.addshape('Chicken Sandwich.gif')
t.shape('Chicken Sandwich.gif')
t.stamp()


t.penup()
t.goto(-100, -200)
t.pendown()
screen.addshape('Pizza.gif')
t.shape('Pizza.gif')
t.stamp()
t.shape("classic")

#Third Slide
round = input("Press Enter to Continue: ")
t.clear()
screen.bgcolor('orange')
t.penup()
t.goto(0, 250)
t.pendown()
t.write('My Hobbies', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 200)
t.pendown()
t.write('1. Basketball', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 150)
t.pendown()
t.write('2. Golf', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 100)
t.pendown()
t.write('3. Video Games', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 50)
t.pendown()
t.write('4. Watching TV', font=("ariel", 30, "italic"), align="center")

#Circle
t.penup()
t.goto(0,-50)
t.pendown()
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.setheading(0)
t.circle(50)
t.end_fill()

t.penup()
t.goto(-100, -200)
t.pendown()
screen.addshape('Bryson.gif')
t.shape('Bryson.gif')
t.stamp()
t.shape("classic")

t.penup()
t.goto(100, -200)
t.pendown()
screen.addshape('nba.gif')
t.shape('nba.gif')
t.stamp()
t.shape("classic")

#Fourth Slide
round = input("Press Enter to Continue: ")
t.clear()
screen.bgcolor('Purple')
t.penup()
t.goto(0, 200)
t.pendown()
t.write('My Favorite Movie', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 150)
t.pendown()
t.write('My Favorite Movie is Rounders', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(100, -200)
t.pendown()
screen.addshape('whiplash.gif')
t.shape('whiplash.gif')
t.stamp()
t.shape("classic")

t.penup()
t.goto(-100, -200)
t.pendown()
screen.addshape('cards.gif')
t.shape('cards.gif')
t.stamp()
t.shape("classic")

#rectangle
t.penup()
t.goto(-50,0)
t.pendown()
t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.end_fill()

#Fifth Slide
round = input("Press Enter to Continue: ")
t.clear()
screen.bgcolor('Purple')
t.penup()
t.goto(0, 200)
t.pendown()
t.write('My Favorite Sport', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(0, 150)
t.pendown()
t.write('My Favorite Sport is Basketball', font=("ariel", 30, "italic"), align="center")

t.penup()
t.goto(-100, -200)
t.pendown()
screen.addshape('Lebron2.gif')
t.shape('Lebron2.gif')
t.stamp()
t.shape("classic")

t.penup()
t.goto(100, -200)
t.pendown()
screen.addshape('Goat1.gif')
t.shape('Goat1.gif')
t.stamp()
t.shape("classic")

t.penup()
t.goto(-30,0)
t.pendown()

t.fillcolor('yellow')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)


t.end_fill()















# t.penup()
# t.goto(0, 0)
# t.pendown()
# screen.addshape('turtle5leg.gif')
# t.shape('turtle5leg.gif')
# t.stamp()
# t.shape('classic')

t.penup()
t.goto(0, -100)
t.pendown()
t.write('', font=("ariel", 30, "italic"), align="center")
round = input("Press Enter to Continue: ")


turtle.done()