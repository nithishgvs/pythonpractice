def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(even_check(10))
    print(even_check(11))
    numbers = range(10)
    even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
    print(even_numbers)
