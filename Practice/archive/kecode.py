#input
keycode = input("What is the keycode?")

#keycode list should be in file
keylist = ["1234", "3425", "3532","9804"]

#procedure
if keycode in keylist:
    message="login success"
else:
    message = "Login error"

#output
print(f"The message is {message}")