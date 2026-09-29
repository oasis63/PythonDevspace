a = [1, 2, 3, 3, 4, 5, 4]

it = iter(a)


print(next(it))
print(next(it))


for val in it:
    print(val)
