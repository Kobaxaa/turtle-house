from turtle import *
#square

speed(200)
color("purple")
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()

#windows
goto(20, 135)
pendown()
color("blue")
begin_fill()
left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
penup()

left(90)
forward(120)
pendown()
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()




















exitonclick()



