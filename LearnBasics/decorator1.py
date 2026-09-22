def to_upper(fun1):
    def inner():
        return fun1().upper()
    return inner


def add_excl(fun1):
    def proce():
        return fun1() + "!"
    return proce



@to_upper
@add_excl
def my_method():
    return "Hellllo"


print(my_method())