#Function Definitions
def Exercise1():
	for x in range(2000 , 3200) :
		if (x % 7 == 0 and x % 5 != 0) :
			print(x, end=",")	

def Exercise2(x):
	if (x == 0):
		return 1
	return x * Exercise2(x-1)

#call Exercise
factorial = int(input("Enter Factorial:"))
print(Exercise2(factorial))

