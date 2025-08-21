fruits = ('banana', 'orange', 'mango', 'lemon')
numbers = (1, 2, 3, 4, 5, 3, 3)

print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])

print('banana' in fruits)
print('apple' in fruits)

print(numbers.count(3))
print(numbers.index(4))

one_item = ('apple',)
print(one_item)

tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

print(tuple3[2:6])
print(tuple3[::-1])

del tuple1
