#lucky number game

import random

x=random.randint(1,100)
y=0
print("welcome to lucky number game")
print("you have 7 attempts to guess the number between 1 and 100")
while y<7:
    z=int(input("please guess the number between 1 and 100:"))
    y=y+1
    if z==x:
        print("congratulations!your guess is correct")
        if y == 1:
           print(f"you  found the lucky number in first attempt")
        else:
            print(f"congratulations!you found the lucky number in {y} attempts")
        break
    elif z<x:
        print("sorry you guess is too low")
    else:
        print("sorry you guess is too high")

else:
      print("sorry, you used all attempts.")
      print(f"the lucky number is {x}")










