a = ["Python", "Java", "C++", "Go"]
b = a
c = a[:]
b[0] = "Code"
c[1] = "Quiz"
count = 0

print(a)
print(b)
print(c)

for x in (a, b, c):
    if x[0] == "Code":
        count += 1

    if x[1] == "Quiz":
        count += 10

print(count)
