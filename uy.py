# 1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Bu hayvon ovoz chiqardi.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} vov-vov qiladi!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} miyovlaydi!")

dog = Dog("Rex")
cat = Cat("Mushuk")
dog.speak()
cat.speak()

# 2
class Transport:
    def __init__(self, model):
        self.model = model
    
    def move(self):
        print("Bu transport harakatlanmoqda.")

class Car(Transport):
    def move(self):
        print(f"{self.model} mashinasi yo‘lda ketmoqda!")

class Bicycle(Transport):
    pass

car = Car("Tesla Model X")
bike = Bicycle("BMX")
car.move()
bike.move()

# 3
class Worker:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def work(self):
        print(f"{self.name} ish qilmoqda.")

class Engineer(Worker):
    def work(self):
        print(f"{self.name} muhandis va loyiha chizmoqda.")

class Doctor(Worker):
    pass

eng = Engineer("Akmal", "Engineer")
doc = Doctor("Laylo", "Doctor")
eng.work()
doc.work()

# 4
class Player:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} o‘yin o‘ynamoqda.")

class Footballer(Player):
    def play(self):
        print(f"{self.name} futbol o‘ynamoqda!")

class ChessPlayer(Player):
    pass

futbolchi = Footballer("Cristiano Ronaldo")
shaxmatchi = ChessPlayer("Magnus Carlsen")
futbolchi.play()
shaxmatchi.play()

# 5
class Pet:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print("Bu uy hayvoni.")

class Parrot(Pet):
    def info(self):
        print(f"{self.name} - bu papugay va gapira oladi!")

class Rabbit(Pet):
    pass

parrot = Parrot("Kesha")
rabbit = Rabbit("Bunny")
parrot.info()
rabbit.info()
