import fire

# In version 1  we exposed all the program's functionality  to the command line.
# By using a dict, we can selectively expose functions to the command line.

def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def foo():
    return "bar"


if __name__ == '__main__':
    fire.Fire({
        'add': add,
        'multiply': multiply,
        'mul': multiply,
    })
