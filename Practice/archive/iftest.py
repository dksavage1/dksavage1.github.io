#test for if pytjon stsatement
grade=91
if grade>90:
    print("you got an A \n")

if grade<70:
    print("you fail")
   
#Example
#BMI = 26

#if BMI>25:
    print("overweight")
#else:
    print("Everything is normal")
#practice
#grade1 = 78
#grade2 = 89
#grade3 = 100
#average = (grade1+grade2+grade3)/3

if average >70:
    print("you pass")
else:
    print("you fail")
#input
Height = float(input("height"))
Weight = float(input("weight"))
#procedure
bmi= 703*weight/(height**2)

if bmi<18.5:
    messahe = "you are underweight"
elif bmi < 25:
    message = "you are normal"
elif bmi <30:
    message = "you are fat"
else:
    message = "beached whale"

#output
print(message)