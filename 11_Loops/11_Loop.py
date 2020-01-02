for i in range(5):
    if (i == 3):
        print("You are breking the loop")
        break
    if(i == 2):
        print("You are skiping i==2")
    if(i == 1):
        pass  # Just do not something
    else:
        print(i)
# An ELSE statment can be used to do a final action after completion of a loop
# this is always cover, unless you end the loop with a BREAK statement
else:
    print("You are in an ELSE statement")


while True:
    for i in range(1, 5):
        if i == 2:
            break  # Will only break out of the inner loop!
