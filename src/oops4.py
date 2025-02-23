class Animal:
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("eating")


class Dog(Animal):
    def __init__(self):
        super().__init__()  # Calls the parent class constructor
        print('Dog Created')

    def who_am_i(self):
        print("Dog")

    def bark(self):
        print("Woof!")


if __name__ == "__main__":
    d = Dog()  # Output: "Animal created" then "Dog created"
    d.who_am_i()  # Output: "Dog"
    d.eat()  # Output: "Eating"
    d.bark()  # Output: "Woof!"
