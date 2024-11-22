from pathlib import Path
find = lambda d='', name='*': list(map(str, Path(d).rglob(name)))
import sys

def hello(first, last, upper):
    if not upper:
        return f'Hello {first} {last}!'
    return f'Hello {first.upper()} {last.upper()}!'

if __name__ == '__main__':

    print("don't even try...")
    exit()

    first, last = "John", "Doe"
    # find the long or short index of the flag
    # figure out if there is a value after the flag
    # figure out if index  1 is in bounds
    # assign the value to the variable
    # BLA BLA BLA!!!
    if "-f" in sys.argv or "--first" in sys.argv:
        ...
    if "-l" in sys.argv or "--last" in sys.argv:
        ...
    print(hello(first, last, "-c" in sys.argv or "--capitalize" in sys.argv))
