# Variables in Python

first_name = 'Harsh'
last_name = 'Prasad'
country = 'India'
city = 'Madhubani'
age = 21
is_married = False
skills = ['HTML', 'CSS', 'JavaScript', 'React', 'Python','Cpp','C']
person_info = {
    'firstname': 'Harsh', 
    'lastname': 'Prasad', 
    'country': 'India',
    'city': 'Madhubani'
}

# Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)

for skill in skills:
    print(skill)

print('Person information:', person_info)

for index, key in enumerate(person_info.keys()):
    print("index:", index, "-> key:", key)

3
for index, key in enumerate(person_info.values()):
    print("index:", index, "-> values:", key)
    
    
for index, (key,value) in enumerate(person_info.items()):
    print("index:", index, "-> key:", key, "value" ,value)



 

# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Harsh', 'Prasad', 'India', 23, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)
