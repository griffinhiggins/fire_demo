import argparse

def hello(first, last, upper):
    if not upper:
        return f'Hello {first} {last}!'
    return f'Hello {first.upper()} {last.upper()}!'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--first', type=str, default='John')
    parser.add_argument('-l', '--last', type=str, default='Doe')
    parser.add_argument('-u', '--upper', action='store_true')
    args = parser.parse_args()
    print(hello(args.first, args.last, args.upper))
