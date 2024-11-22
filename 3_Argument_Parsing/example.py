import fire

# The types of the arguments are determined by their values, rather than by the
# function signature where they're used. You can pass any Python literal from the
# command line: numbers, strings, tuples, lists, dictionaries, (sets are only
# supported in some versions of Python). You can also nest the collections
# arbitrarily as long as they only contain literals.

# To demonstrate this, we'll make a small example program that tells us the type
# of any argument we give it:

def main(obj):
    t = type(obj)
    return obj, t.__name__

fire.Fire(main)
