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

def Exercise7(x , y):
	xArray = []
	for i in range(0 , x):
		yArray = []
		for j in range(0 , y):
			yArray.append(i*j)
		xArray.append(yArray)
	print(xArray)

def Exercise8(x):
    unsortedList = x.split(",")
    sortedList = sorted(unsortedList)
    print(",".join(sortedList))

def Exercise9(lines):
    for item in lines:
        print(item.upper())
    
#call Exercise
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

Exercise9(lines)