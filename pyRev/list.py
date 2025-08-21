empty_list = list()
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux']
countries = ['Finland', 'Estonia', 'Denmark']

print(fruits, len(fruits))
print(vegetables, len(vegetables))
print(animal_products, len(animal_products))
print(web_techs, len(web_techs))
print(countries, len(countries))

fruits[0] = 'Mango'
fruits[1] = 'Apple'
fruits[-1] = 'Lime'
print(fruits)

print('banana' in fruits)
print('Lime' in fruits)

fruits.append('Kiwi')
print(fruits)

fruits.insert(2, 'Papaya')
print(fruits)

fruits.remove('Apple')
print(fruits)

fruits.pop()
print(fruits)

fruits_copy = fruits.copy()
print(fruits_copy)

numbers = [-3, -2, -1, 0, 1, 2, 3]
print(numbers)

fruits.extend(vegetables)
print(fruits)

print(fruits.count('orange'))
print(fruits.index('mango'))

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)
