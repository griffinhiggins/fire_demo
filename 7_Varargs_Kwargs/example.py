import fire

# Fire supports functions that take \*varargs or \*\*kwargs. Here's an example:

def foo(a, *args, b=10, **kwargs):
    print('a:', a)
    print('b:', b)
    print('args:', args)
    print('kwargs:', kwargs)

def bar(first_kwarg=10, second_kwarg=20):
    print('first_kwarg:', first_kwarg)
    print('second_kwarg:', second_kwarg)


if __name__ == '__main__':
    fire.Fire()
