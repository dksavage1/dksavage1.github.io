origin = (0,0,0)

def move(pos):
    (x,y,z)=pos #get xcor ycor
    x=x-1
    y = y+2
    z = z-5
    return (x,y,z)
    #test
current = (4,5,3)
print(move(current))