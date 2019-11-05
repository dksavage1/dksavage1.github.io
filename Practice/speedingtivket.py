#input
Speed = int(input("How fast were you going?"))

#process
if Speed <= 75:
    print("Fine is $0")
elif Speed <80:
    print("Ticket cost is $25")
elif Speed <84:
    print("$100")
elif Speed < 94:
    print("$125")
elif Speed < 99:
    print("$150")
elif Speed < 109:
    print("$500")
elif Speed > 120:
    print("jail")

