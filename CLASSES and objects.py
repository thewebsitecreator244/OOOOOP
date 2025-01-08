from random import choice, randint
from time import sleep


# creating class
class Human:
    # 1-attributes(fields, properties)-variables inside of class
    skin_color = "brown"
    hair_color = "blue"
    eye_color = "red"
    age = 10
    name = "Rèdenter"
    last_name = "Zumàs"
    gender = "male"
    hunger = 50

    # 2-methods-functions inside of class
    def greet(self, other):
        # self-the object itself
        print(f"hello,{other.name} {other.last_name}, my name is {self.name} {self.last_name}, nice to meet you")

    def compare_age(self, other):
        if self.age > other.age:
            print(f"{self.name} is older than {other.name}")
        elif other.age > self.age:
            print(f"{other.name} is older than {self.name}")
        else:
            print("the same age")

    def birthday(self):
        self.age += 1
        print(f"happy birthday, {self.name} is now {self.age}")

    def eat(self, other):
        if self.hunger >= 50:
            print(f"{self.name} is eating")
            self.hunger -= 20
        elif self.hunger < 30:
            print(f"{self.name} is not hungry")
        elif randint(1, 2) == 2:
            print(f"{self.name} ate {other.name}'s food")
        else:
            self.hunger += 20



    def hello(self, other):
        print(f"hello {other.name}")
        print(f"hello {self.name}")


if __name__ == "__main__":
    # creating Objects
    human1 = Human()
    human2 = Human()
    human2.name = "Lavandina"
    human2.last_name = "Flowers"
    human2.gender = "female"
    human2.age = 11
    actions = [human1.compare_age, human2.compare_age, human1.eat, human2.eat, human1.hello, human2.hello]
    print(human1, human2)
    print("characters: ")
    print(human1.name + " " + human1.last_name)
    print(human2.name + " " + human2.last_name)
    print()
    human1.greet(human2)
    human2.greet(human1)
    print()
    secs = 0
    while True:
        action = choice(actions)
        action(human1)
        sleep(1)
        print()
        secs += 1
        if secs % 10 == 0:
            human1.birthday()
        if secs % 11 == 0:
            human2.birthday()
