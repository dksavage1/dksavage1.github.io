mylist = [2,4,6,12,45,20,5,78]



lgsofar=mylist[0]
for num in mylist:
    if num > lgsofar :
        lgsofar = num
    
print(f"The largest number is {lgsofar}")

smsofar=mylist[0]
for num in mylist:
    if num < lgsofar :
        lgsofar = num
    
print(f"The smallest number is {lgsofar}")