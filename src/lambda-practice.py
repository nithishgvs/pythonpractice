def square(num):
    return num ** 2


if __name__ == "__main__":
    print(square(2))
    square = lambda num: num ** 2
    print(square(4))
    even = lambda num: (num % 2) == 0
    print(even(5))
    # Grab first char of a string
    char = lambda str: str[0]
    print(char('Ishitha'))
    # reverse string
    reverse = lambda str: str[::-1]
    print(reverse("Sai"))

    adder = lambda x,y: x+y
    print(adder(1,6))