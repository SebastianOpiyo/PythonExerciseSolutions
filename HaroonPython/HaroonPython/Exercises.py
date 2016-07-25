#Function Definitions
import math
def Exercise1():
	for x in range(2000 , 3200) :
		if (x % 7 == 0 and x % 5 != 0) :
			print(x, end=",")	

def Exercise2(x):
	if (x == 0):
		return 1
	return x * Exercise2(x-1)

def Exercise3(x):
    dict = {}    
    for x in range(1 , x + 1) : 
        dict[x] = x * x
    return dict

def Exercise4(x):
    
    #get into list
    list = x.split(",") 
    
    #print both
    print(list)
    print(tuple(list))
    
class Exercise5(object):
    def __init__(self):
        self.x = ""

    def getString(self):
        self.x = input("Enter String:")

    def printString(self):
        print(self.x.upper())

def Exercise6(x) :
	C = 50
	H = 30
	listOfD = str(x).split(",")
	listOfQ = []
	for D in listOfD:
		Q = str(round(math.sqrt((2 * C * int(D)) / H)))
		listOfQ.append(Q)	
	print(",".join(listOfQ))

#call Exercise
Exercise6(input("Enter comma separate D: "))