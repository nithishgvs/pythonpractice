def main():
    l = []
    for ch in 'word':
        l.append(ch)
    print(l)
    # list comprehension
    y = [letter for letter in 'word']
    print(y)

    lst = [x ** 2 for x in range(0, 11)]
    print(lst)

    even = [number for number in range(0, 11) if number % 2 == 0]
    print(even)

    celcius = [10, 20, 50, 190]

    fahrenheit = [temp * (9 / 5.0) + 32 for temp in celcius]
    print(fahrenheit)
    # Nested list comprehension
    list = [x ** 2 for x in [x ** 2 for x in range(0, 11)]]
    print(list)


# list comprehension allows to build  lists using different notation
# its a one line for loop built out of brackets
if __name__ == "__main__":
    main();
