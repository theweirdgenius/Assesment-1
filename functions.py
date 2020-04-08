# A simple Python function to check 
# whether x is even or odd 
def evenOdd( x ): 
	if (x % 2 == 0): 
		print ("even")
	else: 
		print ("odd")

# Driver code 
evenOdd(2) 
evenOdd(3) 


def swap(x, y): 
	temp = x; 
	x = y; 
	y = temp; 

# Driver code 
x = 2
y = 3
swap(x, y) 
print(x) 
print(y) 


# Python program to demonstrate 
# default arguments 
def myFun(x, y=50): 
	print("x: ", x) 
	print("y: ", y) 

# Driver code (We call myFun() with only 
# argument) 
myFun(10) 


# Python program to demonstrate Keyword Arguments 
def student(firstname, lastname): 
	print(firstname, lastname) 
	
	
# Keyword arguments				 
student(firstname ='Geeks', lastname ='Practice')	 
student(lastname ='Practice', firstname ='Geeks') 

# Python program to illustrate 
# *args for variable number of arguments 
def myFun(*argv): 
	for arg in argv: 
		print (arg) 
	
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 


# Python program to illustrate 
# *kargs for variable number of keyword arguments 

def myFun(**kwargs): 
	for key, value in kwargs.items(): 
		print ("%s == %s" %(key, value)) 

# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')	 

# Python code to illustrate cube of a number 
# using labmda function 
	
cube = lambda x: x*x*x 
print(cube(7)) 


