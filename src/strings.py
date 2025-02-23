import math


def strings():
    print('Hello')
    print("Hello Sai \nHappy day")
    print(len("Hello Sai"))
    s = "Welcome to Python"
    print(s)
    print(s[0])
    print(s[1])
    print(s[1:])
    print(s[:3])
    print(s[:])
    # Grab everything except last letter
    print(s[:-1])
    # Grab last letter
    print(s[-1])
    # Grab everything, but go in steps size of 1
    print(s[::1])
    # Grab everything, but go in steps size of 2
    print(s[::2])
    # Revers string
    print(s[::-1])



def strings2():
    s = "Welcome to Python"
    s += " concatenate me "
    print(s)
    letter = 'z'
    print(letter * 5)
    s = 'Hello'
    print(s.upper())
    print(s.lower())
    print(s.split('e'))
    print(math.sqrt(3))


# Its important to note that strings have an important property known as immutability. This means that once a string is created, the elements within it can not be changed or replaced


if __name__ == "__main__":
    strings2();
    print(math.sqrt(4))
