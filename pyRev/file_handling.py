import os

try:
    
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "students.txt")

    
    with open(file_path, "r") as file:
        data = file.read()
        print(" File contents:")
        print(data)

    
    with open(file_path, "a") as file:  
        file.write("\nHarsh Prasad - Python Learner")
        print("\n New line added to file.")

    
    with open(file_path, "r") as file:
        print("\nUpdated contents:")
        print(file.read())

except FileNotFoundError:
    print("File nahi mili, Harsh. Pehle students.txt banao.")
except PermissionError:
    print("Permission ka issue hai, file open nahi ho rahi.")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("\nProgram khatam, dhanyawaad Harsh.")
