def sumofsquare(x,y,): 
    '''This functions compute the sun of squares'''
    ans = x**2 + y**2
    return ans

#test it
print(sumofsquare(3,4))

def totalsum(x1,x2,x3,x4):
    '''This function computes the sum of the totals'''
    ans = x1 + x2 + x3 + x4
    return ans

#test
print(totalsum(2,3,4,5))

def addN(task,mylist):
    '''Add a new task to end'''
    mylist.append(task)
    return mylist
mylist = [1,2,3,4,5]
print(addN(6,mylist))
print(addN(7,mylist))

def addB(task,mylist):
    '''Update first item of list'''
    mylist[0]=task
    return mylist
mylist = [1,2,3,4,5]
print(addB(9,mylist))