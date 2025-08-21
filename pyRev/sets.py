fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage'}
numbers = {1, 2, 3, 4, 5}

print(fruits)
print(len(fruits))

fruits.add('apple')
fruits.add('lime')
print(fruits)

fruits.update(['kiwi', 'papaya'])
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.discard('pear')
print(fruits)

item = fruits.pop()
print(item, fruits)

fruits.clear()
print(fruits)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))

print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))
