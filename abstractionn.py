# from abc import ABC, abstractmethod

# class Person(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
    
# class English(Person):
#     def speak(self):
#         print("I can speak")

# e = English()
# e.speak()


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

d = Dog()
d.make_sound()
