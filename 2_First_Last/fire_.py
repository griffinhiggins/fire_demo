import fire

def hello(first="John", last="Doe", upper=False):
    if not upper:
        return f'Hello {first} {last}!'
    return f'Hello {first.upper()} {last.upper()}!'

if __name__ == '__main__':
    fire.Fire(hello)
