import turtle

s = turtle.Screen()
t = turtle.Turtle(shape='turtle')
t.color("black","white")
turtle.hideturtle()

t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()

t.goto(-30,135)
t.pendown()
t.dot(25)
t.penup()

t.goto(30,135)
t.pendown()
t.dot(25)
t.penup()

t.goto(-60,60)
t.pendown()
t.setheading(-60)
t.circle(70,120)
t.penup()
