class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"My name is {self.name}. I am {self.age} years old and I study {self.course}.")

    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult.")
        else:
            print(f"{self.name} is not an adult.")


student1 = Student("Harsh Prasad", 21, "Python Programming")
student2 = Student("Amit", 16, "Mathematics")

student1.introduce()
student1.is_adult()

student2.introduce()
student2.is_adult()
