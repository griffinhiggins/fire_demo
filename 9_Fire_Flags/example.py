import fire

def foo(*args):
    '''How does this function work again? Oh LOOK DOCUMENTATION... and its hot a hallucination!!!!'''
    return ' '.join(args)

def bar(a, b, c="moo"):
    '''Some arbitrary function that does some arbitrary stuff...'''
    return a + b if c == "moo" else a * b

if __name__ == '__main__':
    fire.Fire()
