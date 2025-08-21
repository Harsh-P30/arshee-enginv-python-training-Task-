try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Arre bhai, 0 se divide nahi hota!")
except ValueError:
    print("Please enter a valid number, Harsh.")

try:
    marks = int(input("Enter your marks: "))
    percentage = marks / 100 * 100
    print("Your percentage is:", percentage)
except ValueError:
    print("Harsh, marks sirf number mein dalo.")
except Exception as e:
    print("Kuch galat ho gaya:", e)

try:
    file = open("pyRev\\students.txt", "r") 
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File nahi mili, Harsh.")
finally:
    print("Program khatam, dhanyawaad ")


try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise Exception("Harsh, tum abhi vote nahi de sakte!")
    else:
        print("You can vote")
except Exception as e:
    print("Error:", e)
