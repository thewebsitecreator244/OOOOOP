class Cat:
    def __init__(self, says, name, *colors1, eye_color, tail, colors_number):
        self.says = says
        self.name = name
        self.colors = colors1
        self.eye_color = eye_color
        self.tail = tail
        self.colors_number = colors_number

    def meow(self):
        print(
            f"a {self.colors_number} colored cat({self.colors}) with {self.eye_color} eyes, a {self.tail} and the name {self.name} says")
        print(self.says)


Garf = Cat("MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW", "Garfield",
           "orange with brown stripes", "white pawed", eye_color="green", tail="pom-pom", colors_number=3)
Garf.meow()
