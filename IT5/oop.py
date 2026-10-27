# Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name # Attrirvutes
        self.__age = age  # Private attribute
        self.address = "" # Public attribute
    def __setname(self, name): #Methods / Behavior
        self.name = name
    def getName(self):
        return self.name
    def getAge(self):
        return self.__age
    def __str__(self):
        return f"{self.name} is {self.__age} years old"        

#p1 = Person(name='Ryo', age=17)
#print(p1)
#print(p1.getAge())
#print(p1.getName())    

#Inheritance
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def move(self):
        print("Moving Student. . .")

#Polymorphism
class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def move(self):
        print("Moving Teacher. . .")

for x in Teacher('Nijika', 18), Student('Ryo', 17):
    x.move()
