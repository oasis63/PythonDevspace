def my_function(x):
    print("dict.fromkeys : ", dict.fromkeys(x))
    return list(dict.fromkeys(x))
  

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)


