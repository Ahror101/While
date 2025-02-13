# Misol 1
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.speak()) 
print(cat.speak())  

# Misol 2
class Film:
    def move(self):
        return "Moving"

class Car(Film):
    def move(self):
        return "Car is moving"

class Bike(Film):
    def move(self):
        return "Bike is moving"

car = Car()
bike = Bike()
print(car.move()) 
print(bike.move())  

# Misol 3
class Person:
    def work(self):
        pass

class Teacher(Person):
    def work(self):
        return "Teaching students"

class Doctor(Person):
    def work(self):
        return "Treating patients"
teacher = Teacher()
doctor = Doctor()
print(teacher.work()) 
print(doctor.work()) 

# Misol 4
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def init(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def init(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Foydalanish
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(circle.area())  # 78.5
print(rectangle.area())  # 24

# Misol 5
class Employee:
    def get_salary(self):
        pass

class Developer(Employee):
    def get_salary(self):
        return 8000

class Manager(Employee):
    def get_salary(self):
        return 12000
dev = Developer()
mgr = Manager()
print(dev.get_salary()) 
print(mgr.get_salary()) 


# Misol 1
class A:
    def method_a(self):
        return "Method from A"

class B:
    def method_b(self):
        return "Method from B"

class C(A, B):
    pass
obj = C()
print(obj.method_a())  
print(obj.method_b())  

# Misol 2
class Flyable:
    def fly(self):
        return "Flying"

class Swimable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimable):
    pass
duck = Duck()
print(duck.fly())  
print(duck.swim())  

# Misol 3
class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def move(self):
        return "Wheels rolling"

class Car(Engine, Wheels):
    pass

# Foydalanish
car = Car()
print(car.start())  
print(car.move()) 

# Misol 4
class Parent1:
    def feature1(self):
        return "Feature from Parent1"

class Parent2:
    def feature2(self):
        return "Feature from Parent2"

class Child(Parent1, Parent2):
    pass

child = Child()
print(child.feature1())  
print(child.feature2()) 

# Misol 5
class Writer:
    def write(self):
        return "Writing a book"

class Speaker:
    def speak(self):
        return "Giving a speech"

class Author(Writer, Speaker):
    pass
author = Author()
print(author.write())  
print(author.speak())