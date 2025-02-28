def fahrenheit(T):
    return (9 / 5) * T + 32


if __name__ == "__main__":
    celcius = [0, 22, 33, 99]
    results = list(map(fahrenheit, celcius))
    print(results)

    results2 = list(map(lambda T: (9 / 5) * T + 32, celcius))
    print(results2)

    a = [1, 2, 3]
    b = [5, 6, 7]
    c = [7, 8, 9]
    results3 = list(map(lambda x, y, z: x + y + z, a, b, c))

    print(results3)
