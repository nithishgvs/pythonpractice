def main2():
    try:
        2 + 's'
    except:
        print('TypeError encountered')
    finally:
        print('Finally print')


def main():
    try:
        f = open('test123.txt', 'r')
        f.write('sample text')
    except Exception as e:  # Catches all exceptions
        print(f"An error occurred: {e}")
    finally:
        print('Finally print')


def askInt2():
    try:
        val = int(input('Please enter an integer: '))
    except:
        print('Looks you did not enter an integer')
        val = int(input('Try again pls input an integer: '))
    finally:
        print('Finally block executed')

    print(val)


def askInt():
    while True:
        try:
            val = int(input('Please enter an integer: '))
        except:
            print('Looks you did not enter an integer')
            continue
        else:
            print('Correctly got an integer')
            break
        finally:
            print('Finally block executed')

    print(val)


if __name__ == "__main__":
    askInt()
