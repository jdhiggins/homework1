from turtle import *
def twosides_background():
  forward(270)
  left(90)
  forward(180)
  left(90)

penup()
goto(-135,-90)

pendown()
for i in range(2):
  twosides_background()
penup()

goto(-135,0)

pendown()
pencolor("red")
fillcolor("red")
begin_fill()
forward(270)
left(90)
forward(90)
left(90)
forward(270)
left(90)
forward(90)
end_fill()

penup()
goto(-110,45)
pencolor("white")
fillcolor("white")
pendown()
begin_fill()
circle(30)
end_fill()
penup()
goto(-97,45)
pendown()
fillcolor("red")
pencolor("red")
begin_fill()
circle(27)
end_fill()
penup()
goto(-40,52)
setheading(0)

def star():
  pendown()
  color("white", "white")
  begin_fill()
  for _ in range (5):
    right(180 - 36)
    forward(12)
  end_fill()
  penup()
  right(180 - 36)
  forward(45)
for i in range(5):
  star()

goto(-180,-180)
