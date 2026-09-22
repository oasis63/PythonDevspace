def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

# myfunc()


def counter():
    x = 1

    def inner_counter():
        nonlocal x
        print(x)
        x=x+1
        # return x
    
    return inner_counter



c1 = counter()
c1()
c1()
c1()



def fun1():
    global yy
    yy = 300
    print(yy)

fun1()

print(yy)

