# for loop
'''sum = 0
for i in range(23,100):
    sum = sum + i
    #sum += i
    print(f"add  {i}")

print(f"the sum is {sum}") '''
'''
sum = 0
for i in range(1,100,2):
    sum = sum + i
    #sum += i
    print(f"add square of {i}")

print(f"the sum is {sum}")'''

'''
sum = 0
for i in range(1,100):
    sum = sum + i*i
    #sum += i
    print(f"add square of {i}")

print(f"the sum is {sum}")
'''

'''sum = 0
for i in range(2,100,2):
    sum = sum + 1/i
    #sum += i
    print(f"add one over {i}")

print(f"the sum is {sum}")
'''

sum = 0
for i in range(1,101):
    if i % 10 == 0:
        print("skip")
    else:
        sum = sum + i
    #sum += i
    print(f"add sum of {i}")

print(f"the sum is {sum}")