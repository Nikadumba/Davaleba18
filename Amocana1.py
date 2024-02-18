

def decorator(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        if num <= 0:
            raise ValueError("Number is negative or zero!")
        else:
            print(f"Number is positive: {num}")
    return wrapper 


@decorator
def return_num(n):
    return n


return_num(100)
