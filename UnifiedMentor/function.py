
# PYTHON FUNCTIONS

# A function is a block of code which only runs when it is called
# advanced Functions- Lambda , map , zip

def func():
    print("Hello World")
    
func() 

def funn(name):
    print("Hello World " +name)
    
funn("Vishakha")    
    
    
def add(a,b,c) :
    print(a+b+c)

add(5,8,3)    
    
 # using lambda function 
 
multiply = lambda a,b,c:print(a*b*c)


multiply(7,8,8)    
    
# map function

nums=[1,2,3,4,5,]
def sq(n):
    return n*n
    
square = map(sq,nums)    
print(list(square))    

# zip function

name=["Vishakha", "Ashvani", "Kanhaiya"]

ID=[4,1,3]

mapped=zip(name,ID)
print(list(mapped))
