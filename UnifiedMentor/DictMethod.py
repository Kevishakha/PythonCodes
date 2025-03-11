# Dict --  key value pairs
# A dictionay is a collection which is ordered , changable and donot allow duplicates unique key
# Methods and functions can used 
# items()
# get()
# fromkeys()
# keys()
# clear()
# popitem()
# pop()
# values()
# update()
# copy()
# setdefault()
car={'name':'Vishakha','class':'college','age':21}
print(car.get('name'))
print(car.items())
print(car.keys())
print(car.values())
print(car.popitem())
print(car)
print(car.pop('class'))
print(car)
car.update({'color':'red'})  # pay attention
print(car)
