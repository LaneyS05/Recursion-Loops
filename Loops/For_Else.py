# if successful is changed to equal False 
# the else statement will execute
successful = True
for number in range(3):
    print("hello")
    if successful:
        print("Successful")
        break
else:
    print("attemted 3 times and failed")