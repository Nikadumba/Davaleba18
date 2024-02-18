

def decorator(func):
    def wrapper(*args, **kwargs):
        num = args[0] - args[1] - 1
        if num < 0:
            raise ValueError("Insufficient balance!")
        else:
            print(f"Balance after transaction: {num}")
    return wrapper 


@decorator
def transaction(balance, amount):
    return balance - amount


transaction(100, 90)
