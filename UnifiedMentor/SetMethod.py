# Sets are used to store multiple items in a single variable
# Sets are written with curly braces
# Python Sets 
# isuperset()
# copy()
# clear() and add()
# issubset()
# difference()
# intersection()
# union()
# remove()
# discard()

fruits={'apple','cherry','banana'}
fruits.add('orange')
print(fruits)
fruits.pop()
print(fruits)
fruits.remove('banana')
print(fruits)
fruits.add('orange')
print(fruits)
x={'apple','banana','cherry','date'}
y={'google','amazon','china','apple'}
print(x.difference(y))  # all from x except common
print(y.difference(x))
print(x.intersection(y))  # only common
print(x.union(y))   # all from y and common
print(y.union(x)) 
x.update(y)
print(x)
print(y)
