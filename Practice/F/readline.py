'''
#readbyline
f = open("keycodes.txt","r")
keycodelist=[]
for i in range(1,155):
    newcode = f.readline()
    keycodelist.append(newcode)
while newcode != "":
    newcode = f.readline()
    keycodelist.append(newcode)
'''
for newcode in f:
    keycodelist.append(newcode[:-1])
#check user coed correct
usercode = input("Enter the code")
if usercode in keycodelist:
    print("Success")
else:
    print("Fail")
#print
print(keycodelist)