def count_evens(mylist):
    numeven = 0
    for number in mylist:
        if number%2== 1:
            numeven +=1
    return numeven


print(count_evens([2,2,7,9,16,0]))