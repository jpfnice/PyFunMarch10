
import random

secret=random.randint(1,100)

print(secret)

currentNumberOfAttempts=0

while currentNumberOfAttempts < 6:
    #currentValue=input("Enter an int in the range [1,100] (1/6): ")
    while True:
        currentValue=input(f"Enter an int in the range [1,100] ({currentNumberOfAttempts+1}/6): ")
        try:
            currentValue=int(currentValue)
            break
        except:
            print("Wrong value given: ", currentValue, "should be an int")
    
    if currentValue == secret:
        print ("Bingo ! You've found the secret number")
        break
    elif currentValue > secret:
        print("Too large !")
    elif currentValue < secret:
        print("Too small !")   
    currentNumberOfAttempts = currentNumberOfAttempts + 1
else:
    print("The secret number was:", secret)