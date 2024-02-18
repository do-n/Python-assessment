class Fruit:
    def __init__(self, name, color, prize):
        self.name = name
        self.color = color
        self.prize = prize

    def display_fruit(self):
        print(f"My favourite fruit is  {self.name}"f" because it's  Color is {self.color}"f" and it costs {self.prize}")



fruit1 = Fruit("Apple", "Red", 50)
fruit2 = Fruit("Orange", "Orange", 30)
fruit3 = Fruit("Mangoe", "Green", 50)
fruit4 = Fruit("Watermelon", "Red", 150)
fruit5 = Fruit("Pineapple", "Brown", 100)

fruit1.display_fruit()
fruit2.display_fruit()
fruit3.display_fruit()
fruit4.display_fruit()
fruit5.display_fruit()