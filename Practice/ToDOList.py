#todolist


todolist = ['cheese','spaghetti','apple']
task = input("what is your task?")
Prior1 = input("what priority is your task?")

if Prior1 == "high":
    todolist[0:0]=[task]
else:
    todolist.append(task)



'''def addN(task,todolist):
    Add a new task to end
    todolist.append(task)
    return todolist
todolist = ['cheese','spaghetti','apple']
print(addN(task,todolist))


def addB(Prior1,todolist):
    Update first item of list
    todolist[0]=Prior1
    return todolist
todolist = ['cheese','spaghetti','apple']
print(addB(Prior1,todolist)) '''

print(todolist[0:3])