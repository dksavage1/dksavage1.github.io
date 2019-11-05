#nestloop
salary = int(input("your salary:"))
onjob = int(input("years on job:"))

#nest if
if salary < 40000:
    if onjob > 5:
        print("qualify")
    else:
        print("not qualify")
    #do sth
elif salary < 60000:
    if onjob > 25:
        print("qualify")
    else:
        print("not qualify")
    # do sth

