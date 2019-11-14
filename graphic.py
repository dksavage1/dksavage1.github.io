import turtle

win = turtle.Screen() #get the playground
cheese = turtle.Turtle() #one object
Provo = turtle.Turtle() #another

#action 
for i in range(7):
    cheese.forward(100)
    cheese.left(100)


#wait for close
win.mainloop()