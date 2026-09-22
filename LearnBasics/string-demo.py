s1 = "abcdef"

print(s1)

print(s1[2:])


for i in range(len(s1)):
    print(s1[i:])


s1 = s1[:2] + "hello" + s1[2:]

print("updated string s1 :  ", s1)


print("for high string manipulations, convert string to list")

list1 = list(s1)

print(list1)

for i in range(len(list1)):
    list1[i] = list1[i].upper()

s2 = "".join(list1)

print(s2)

rev = s2[::-1]

print("reversed string ", rev)


s3 = "banana"

print(f"remove characters from string {s3}")

s3 = s3.replace("a", "")

print(s3)


a = 3
b = 7

print(a, "-" * 3, b)

a, b = b, a

print(a, "-" * 3, b)


print("simple string manipulation : ")
c = chr(65)

print(c)

x = ord("A")

print(x)
