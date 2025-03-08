print("Try programiz.pro")
#  for loop
# It is used for iterating over a sequence(that is either a list, a tuple, a dictionary, a set, or a string).
# Using Break & Continue  Keyword

fruits=['Apple','Banana','Cherry','pie','mango']
for i in fruits:
    print(i)
    if i=="Banana":
        continue
    if i=="mango":
        break
    
# while loop:- With the while loop we can execute set of statements as long as a condition is true    


num=1
while num<=10:
    if num==5:
        num +=1
        continue
    if num==10:
        break
    print(num)
    num +=1
