class Car:
    def __init__(self, brand, model, color):
        # init - class constructor
        self.brand = brand
        self.model = model
        self.color = color
        self.going = False
        self.locked = True
        self.speed = 0
        self.dir = "Nowhere"

    def info(self):
        print(f"a {self.color} {self.brand} {self.model} is", end=" ")
        if self.going:
            print(f"going at {self.speed} mph {self.dir}")
        else:
            print("staying", end=" ")
            if self.locked:
                print("locked")
            else:
                print("unlocked")

    def unlock(self):
        self.locked = False
        print(f"unlocking a {self.color} {self.brand} {self.model}")

    def lock(self):
        self.locked = True
        print(f"locking a {self.color} {self.brand} {self.model}")

    def drive_forward(self):
        if self.dir != "backward":
            if not self.locked:
                self.going = True
                self.speed += 10
                self.dir = "forward"
        elif self.locked:
            print(f"{self.brand}, {self.model} is locked")
        elif self.dir == "backward":
            print("this car is driving backward")

    def brake(self):
        if self.speed > 0:
            self.speed -= self.speed
            print("braaaaaaaaake")
            self.dir = "Nowhere"

    def drive_back(self):
        if self.dir != "forward":
            if not self.locked:
                self.going = True
                self.speed += 10
                self.dir = "backward"
        elif self.locked:
            print(f"{self.brand}, {self.model} is locked")
        elif self.dir == "forward":
            print("this car is driving forward")


if __name__ == "__main__":
    car1 = Car("Mercedes", "Benz", "black")
    car2 = Car("Bmw", "Wmb", "cyan")

    while True:
        command = input("enter command: ").lower().strip()
        if command == "w":
            car1.drive_forward()
        elif command == "l":
            car1.lock()
        elif command == "u":
            car1.unlock()
        elif command == "s":
            car1.drive_back()
        elif command == "b":
            car1.brake()
        car1.info()
