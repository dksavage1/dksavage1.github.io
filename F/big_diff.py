# Write python function that given an array length 1 or more of ints, 
# return the difference between the largest and smallest values in the array. (Do not use build in python function).
#  Please name your function big_diff and your file bigdiff.py
'''big_diff([10, 3, 5, 6]) → 7'''
#big_diff=([10, 3, 5, 6])

def big_diff(mylist):
    ''' function '''
    lgsofar=mylist[0]
    for num in mylist:
        if num > lgsofar :
            lgsofar = num
        
    print(f"The largest number is {lgsofar}")

    smsofar=mylist[0]
    for num in mylist:
        if num < smsofar :
            smsofar = num
    print(f"The smallest number is {smsofar}")

    difference=lgsofar - smsofar

    print(f"The difference between largest and smallest is {difference}")     

#test function 
big_diff([2, 10, 7, 2])
    
'''
#process
difference = int(lgsofar) - int(smsofar)

print(f"The smallest number is {smsofar}")
print(f"The difference between largest and smallest is {difference}")

def largestnum():
    for num in big_diff:
'''