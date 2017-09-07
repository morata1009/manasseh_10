import random
i=0
r=0
while i<=100:
	roll=int(input("press 4 to roll dice"))
	if roll==4:
		r=random.randint(1,6)
		i=i+r 
		print("you got :",r)
		print("your position is:",i)
		if (i==3):
			i=34
			print("congrats! you got a ladder to 34")
		elif (i==8):
		    i=37
		    print("congrats! you got a ladder to 37")
		elif (i==40):
		    i=68
		    print("congrats! you got a ladder to 68")
		elif (i==52):
		    i=81
		    print("congrats! you got a ladder to 81")
		elif (i==76):
		    i=97
		    print("congrats! you got a ladder to 97")
		elif (i==11):
			print("sorry you got a snake down to 2")
			i=2
			print("sorry you got a snake down to")
		    



	