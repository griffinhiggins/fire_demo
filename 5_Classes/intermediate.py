import fire

# Why might you prefer  a class over an object? One reason is  that you can pass
# arguments  for  constructing the  class  too,  as  in this  broken  calculator
# example.

# Unlike  calling ordinary  functions, which  can be  done both  with positional
# arguments and named arguments (--flag syntax), arguments to __init__ functions
# must  be  passed  with  the  --flag   syntax.  See  the  section  on  [calling
# functions](#calling-functions) for more.

class BrokenCalculator():

    def __init__(self, offset=1):
        self._offset = offset

    def add(self, x, y):
        return x + y + self._offset

    def multiply(self, x, y):
        return x * y + self._offset


if __name__ == '__main__':
    fire.Fire(BrokenCalculator)
