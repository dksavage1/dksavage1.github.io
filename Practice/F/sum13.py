#Write python function that return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky,
#so it does not count and numbers that come immediately after a 13 also do not count. Please name your function sum13 and your file sum13.py
'''sum13([1, 2, 2, 1, 13]) → 6'''
'''sum = 0
for i in range(23,100):
    sum = sum + i
    #sum += i
    print(f"add  {i}")'''

'''def sum(mylist):
    for sum in mylist[0]:
       if sum = mylist
       print(f"sum of the numbers is{sum}")'''

sum = 0      
def sum(mylist):
       
for i in range(mylist):
       sum % 13 == 0
       print("skip")
else:
       sum = sum + i
    #sum += i
print(f"sum of {sum}")


'''
for i in range(6):
    if i % 10 == 0:
        print("skip")
    else:
        sum = sum + i
    #sum += i
    print(f"add sum of {i}")
'''
mylist=([1, 2, 2, 1, 13])