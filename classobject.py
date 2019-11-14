#define a class
class human:
    #initialize atribute/properties name,age
    def __init__(self,name,age):
        self.name = name #"dek"
        self.age= age #21
    #method
    def laugh(self):
        print(f"{self.name}",end="")
        for i in range(5):
            print(":-)",end="")
        print()

    def cry(self):
        print(f"{self.name}",end="")
        for i in range(5):
            print("D':",end="")
        print()
#build an object
I = human("dek",21)
he = human("MAT", 8000)
I.laugh()
he.laugh()
I.cry()
he.cry()