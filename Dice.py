#!/usr/bin/python3
import random
i=0
while(i<=100):
    n=input("Press 4 to roll the dice: ")
    if(n==4):
        r=random.randint(1,6)
        i=i+r
        print("You got :",r)
        print("Your position is: ",i)
        if (i==3):
            i=34
            print("Congrats! You got a ladder to 34")
        elif (i==8):
            i=37
            print("Congrats! You got a ladder to 37")
        elif (i==40):
            i=68
            print("Congrats! You got a ladder to 68")
        elif (i==52):
            i=81
            print("Congrats! You got a ladder to 81")
        elif (i==76):
            i=97
            print("Congrats! You got a ladder to 97")
        elif (i==11):
            print("Sorry you got a a snake down to 2")
            i=2
        elif (i==25):
            print("Sorry you got a a snake down to 4")
            i=4
        elif (i==38):
            print("Sorry you got a a snake down to 38")
            i=9
        elif (i==65):
            print("Sorry you got a a snake down to 46")
            i=46
        elif (i==89):
            print("Sorry you got a a snake 89")
            i=70
        elif (i==93):
            print("Sorry you got a a snake 64")
            i=64
    if (i>=94):
        if ((i+r)==100):
            print("Congrats! You've won!")
        else:
            print("Roll again! ")