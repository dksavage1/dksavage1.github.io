mylogin = {"mike":"mike@camper","mirnie":"cheiii","jj":"mack"}
 #input fro m user
username = input("enter your username: ")

'''if username in mylogin:
     print(f"{username} valid")
else:
    print(f"{username} does not exist")'''

while username not in mylogin:
    print(f"{username} does not exist")
    username = input("enter your username: ")

