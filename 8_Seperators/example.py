import fire

# You can use a separator to indicate  that you're done providing arguments to a
# function. All arguments after the separator will be used to process the result
# of the function, rather than being  passed to the function itself. The default
# separator is the hyphen `-`.

def foo(*args):
    return ' '.join(args)

if __name__ == '__main__':
    fire.Fire(foo)
