class Sample:
    pass


class Dog:
    # Class Object attribute
    species = 'mammal'

    def __init__(self, breed, name, fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur


if __name__ == "__main__":
    x = Sample()
    print(x)
    dog = Dog(breed='Lab', name='Sam')
    print(dog.breed)
    print(dog.species)
    print(dog.name)
    print(dog.fur)
