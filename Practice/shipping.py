#function
def shippingrate(weight):
    '''chicken legs'''
if weight<=2:
    shippingrate = .01
elif weight <= 6:
    shippingrate = .02
else:
    shippingrate = "no"
return shippingrate

#test functions
print(shippingrate(10))