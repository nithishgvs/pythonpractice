from collections import namedtuple


def namedtuple_prac():
    # Define a named tuple called 'Person'
    Person = namedtuple('Person', ['name', 'age', 'city'])

    # Create instances
    p1 = Person(name='Alice', age=25, city='New York')
    p2 = Person(name='Bob', age=30, city='San Francisco')

    print(p1.name)  # Alice
    print(p2.age)  # 30
    print(p1.city)  # New York

    Dog = namedtuple('Dog', 'name age color')
    d1 = Dog('puppy', 2, 'brown')
    print(d1.age)


def test_named_tuple():
    namedtuple_prac()
