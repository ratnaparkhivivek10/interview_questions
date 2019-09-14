# Decorate div function to raise ValueError when b=0
def decorator(func):
    def wrapper(a, b):
        if b == 0:
            raise ValueError
        return a/b
    return wrapper


@decorator
def div(a, b):
    return a/b



print(div(10, 5))
print(div(7, 0))