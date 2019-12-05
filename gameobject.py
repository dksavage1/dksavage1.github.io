import turtle
import random
wn = turtle.Screen()
wn.addshape('mario.gif')

class player(turtle.Turtle):
    #initialize
    def __init__(self,shape,color):
        super().__init__(shape)
        self.color(color)
    #special method
    def goLeft(self):
        self.seth(180)
        self.forward(10)
    def goRight(self):
        self.seth(180)
        self.forward(10)
    def move(self):
        deg = random.randint(0,360)
        movement = random.randint(10,60)
        self.forward(movement)
        self.goLeft(deg)
        self.goRight(deg)
        wn.ontimer(self.move(),2000)

I = player("mario.gif","red")
He = player("turtle","Green")
She = player("turtle","Red")

wn.onkey(I.goLeft,"Left") 
wn.onkey(He.goLeft,"a")   
wn.onkey(She.goRight,"d")



#listen
wn.listen()

#keeep going
wn.mainloop()