import math
class quadratic:
    def __init__(self,a,b,c):
        self.a=a #check a is not 0
        self.b=b
        self.c=c
    def root(self):
        D = self.b**2 - 4 * self.a * self.c
        x1 =( -self.b + math.sqrt(D))/(2*self.a)
        x2 =( -self.b - math.sqrt(D))/(2*self.a)
        return(x1,x2)

    def vertex(self):
        x = -self.b/(2)

#buildobject
fun1 = quadratic(1,0,-1)
fun2 = quadratic(16,4,16)
print(f"Root of this function is {fun2.root()}")