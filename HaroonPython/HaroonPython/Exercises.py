#Function Definitions
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
    

#call Exercise
x = input("Enter sequence: ")
Exercise4(x)
