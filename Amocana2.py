

class Functor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        num = self.func(*args, **kwargs)
        if num <= 0:
            raise ValueError("Number is negative or zero!")
        else:
            print(f"Number is positive: {num}")


def return_num(n):
    return n

my_functor = Functor(return_num)

my_functor(100)
