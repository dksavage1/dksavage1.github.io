import turtle

win = turtle.Screen() #get the playground
cheese = turtle.Turtle() #one object
Provo = turtle.Turtle() #another

#action 
'''for i in range(7):
    cheese.forward(100)
    cheese.left(100)'''

'''for i in range(200,18,-6):
    cheese.forward(i)
    cheese.right(100)
    cheese.left(15)'''
##keep moving until edge of screen
x=cheese.xcor()
while x < win.window_width()/2-50:
    cheese.penup()
    cheese.forward(5)
    cheese.pendown()
    x=cheese.xcor()
    
#wait for close
win.mainloop()