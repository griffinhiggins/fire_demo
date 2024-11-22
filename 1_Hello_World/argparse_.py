import argparse

def hello(name):
    return f'Hello {name}!'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    args = parser.parse_args()
    print(hello(args.name))
