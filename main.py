tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str = ''.join(tup)
print(str)

myDict = {'name': 'John', 'country': 'Norway'}
mySeparator = ', '
y = myDict.values()
x = mySeparator.join(myDict.values())
print(x)
print(y)

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.setdefault('model', 'Bronco')
print(x)
print(car)