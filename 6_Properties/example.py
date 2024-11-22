import fire
from airports import airports

# In the examples we've looked at so far, our invocations of `python example.py`
# have  all run  some function  from the  example program.  In this  example, we
# simply access a property.


class Airport():

    def __init__(self, code):
        self.code = code
        self.name = dict(airports).get(self.code)
        self.city = self.name.split(',')[0] if self.name else None


if __name__ == '__main__':
    fire.Fire(Airport)
