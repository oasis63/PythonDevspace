def test(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

test(10, 20, 30, name="Rajesh", age=28)