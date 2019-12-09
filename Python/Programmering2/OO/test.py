
# Klassarv.

class Person():
    name : str
    age : int
    height : int

    def __init__(self, n, a, h):
        self.name = n
        self.age = a
        self.height = h

    def __str__(self):
        return "My name is:" + self.name

class Student(Person):
    
    def __str__(self):
        return self.name + " is " + str(self.age) + " years old "


p = Student("kalle", 28, 180)

print(p)

