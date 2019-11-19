import turtle
win = turtle.Screen()
me = turtle.Turtle()

'''def recurG(length):
    #base case
    if length <10:
        return
    #general case
    else:
        me.forward(length)
        me.left(80)
        recurG(length-10)
        me.right(32)
        recurG(length/5)

recurG(200)'''

def koch(t,order,size):
    #base case
    if order<=0:
        t.forward(size)
    else:
        koch(t,order-1,size/3)
        t.left(90)
        koch(t,order-1,size/3)
        t.right(90)
        koch(t,order-1,size/3)
        t.left(50)
        koch(t,order-1,size/3)
koch(me,3,500)