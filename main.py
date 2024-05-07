class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Я тварина. Моє ім'я {self.name} і я маю {self.age} роки."

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        return "Гав Гав!"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        return "Мяу Мяу!"

if __name__ == "__main__":
    my_dog = Dog("Rex", 3, "Labrador")
    my_cat = Cat("Whiskers", 2, "Gray")

    print(my_dog.introduce()) 
    print(my_dog.bark())       

    print(my_cat.introduce())
    print(my_cat.meow()) 
