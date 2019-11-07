#find lowest of list

def lowest(scorelist):
    lowests=scorelist[0]
    for num in scorelist:
        if num < lowests :
            lowests = num
    return lowests

#find total, then drop lowest, do average

def specialA(scorelist):
    sum = 0
    for num in scorelist:
        sum = sum + num
    ans = (sum - lowest(scorelist))/(len(scorelist)-1)
    return ans
#read data from files
print(lowest([10,9,10]))
print(specialA([10,9,10]))