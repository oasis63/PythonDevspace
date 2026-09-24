
# *list
#  ↓
# unpack the list
#  ↓
# individual elements


numbers = [10, 20, 30]

print(*numbers)


print(numbers)




# from collections import defaultdict

# a, b = map(int, input().split())

# list_map = defaultdict(list)

# i = -1

# while a > 0:
#     a -= 1
#     i += 1

#     word = input()
#     list_map[word].append(i + 1)

# while b > 0:
#     b -= 1

#     word = input()

#     if word in list_map:
#         print(*list_map[word])
#     else:
#         print(-1)