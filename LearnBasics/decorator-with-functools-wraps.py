from functools import wraps


def to_upper(fun1):
    @wraps(fun1)
    def inner():
        return fun1().upper()

    return inner


def add_excl(fun1):
    @wraps(fun1)
    def proce():
        return fun1() + "!"

    return proce


@to_upper
@add_excl
def my_method():
    """Says hello"""
    return "Hellllo"


print(my_method())

print(my_method.__name__)
print(my_method.__doc__)
print(my_method.__module__)
