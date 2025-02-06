import json
from user_class import *

u = User("A", 12345)
u2 = User("Shror", 2908)
path = "main.json"

menu = ("1. Kirish\n"
        "2. Ko'rish\n")

def read():
    with open(path, "r") as file:
         data = json.load(file)
    return [User.dict_to(d) for d in data]

def write(data):
    with open(path, "w") as file:
        json.dump([obj.to_dict() for obj in data], file, indent=4)

while True:
    print(menu)
    choice = input("enter num: ")

    if choice == "1":
        users = read()
        users += [u, u2]
        write(users)
        print("data saved.")

    elif choice == "2":
        users = read()
        for user in users:
            print(user)