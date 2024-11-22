import fire

# The simplest way  to expose multiple commands is to  write multiple functions,
# and then call Fire.

# You'll notice that Fire correctly parsed `10` and `20` as numbers, rather than
# as strings. Read more about [argument parsing here](#argument-parsing).

def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


if __name__ == '__main__':
    fire.Fire()
