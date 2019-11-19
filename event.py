import turtle
wn = turtle.Screen()
me = turtle.Turtle()
#me.color(red)
#action goup
def goup():
    me.seth(90)
    me.forward(50)
def goleft():
    me.seth(180)
    me.forward(50)
def goright():
    me.seth(45)
    me.forward(50)
def godown():
    me.seth(0)
    me.forward(50)
def gored():
    me.color("red")
def gogreen():
    me.color("green")
#binding
wn.onkey(goup,"Up")
wn.onkey(goleft,"Left")
wn.onkey(goright,"Right")
wn.onkey(godown,"Down")
wn.onkey(gored,"R")
wn.onkey(gogreen,"G")
#listen
wn.listen()

#kep going
wn.mainloop()