# Regular function
def hello():
    return 'Hi Jose!'


# Function taking another function as an argument
def other(func):
    print('Other code goes here!')
    print(func())


# A function that needs a decorator
def func_needs_decorator():
    print('This function needs a decorator')


# Creating a decorator function
def new_decorator(func):
    def wrapper_function():
        print('Code here before executing the func')
        func()  # Call the original function
        print('Code executes after the func')

    return wrapper_function  # Return the wrapper


# Applying the decorator using the @ syntax
@new_decorator
def decorated_function():
    print('This function is now decorated')


def test_dec():
    # Call `other()` with `hello` function
    #other(hello)  # ✅ Works correctly
    decorated_function()
    # Call decorated function
    #decorated_function()  # ✅ Correct way to use decorators


if __name__ == "__main__":
    decorated_function()
