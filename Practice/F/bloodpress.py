#High Blood Pressure: Write a python program that calculate the average systolic blood pressure readings in a given list. 
#And it will display blood pressure categories based on the following guideline: 
#if the average systolic blood pressure is higher than 180, it falls within the Hypertensive crisis stage that requires immediate medical attention.
#if the average systolic blood pressure is 140 to < = 180, it falls within Hypertension Stage 2 that may require medication.
#if the average systolic blood pressure is 130 to < 140, it falls within Hypertension Stage 1 that may require life style changes.

def totalsum(bloodP):
    average = bloodP
    return average

def bloodP(int):
    if bloodP > 180:
        print("call 911")
    elif bloodP < 140:
        print("Stage 2")
    elif bloodP < 130:
        print("Stage 1")

 


print(bloodP([132,143,139,146,150,124])) 
