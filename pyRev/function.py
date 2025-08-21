def greet():
    print("Namaste Harsh Prasad!")

greet()


def greet_user(name):
    print("Namaste", name)

greet_user("Harsh")
greet_user("Prasad")


def add_numbers(a, b):
    return a + b

print(add_numbers(10, 25))
print(add_numbers(45, 55))


def square(number):
    return number * number

print(square(7))


def is_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_even(14))
print(is_even(9))


def greet_many(*names):
    for n in names:
        print("Hello", n)

greet_many("Harsh", "Amit", "sonu")


def person_info(name, age, state="Bihar"):
    print(name, age, state)

person_info("Harsh Prasad", 21, "Jharkhand")
person_info("Harsh Prasad", 21)
