items = ["apple", "banana", "orange"]
prices = [1.2, 0.5, 2.5]
quanities = [20, 30, 40]

for item, price, quanity in zip(items, prices, quanities):
    print(f"The price of {item} is ${price} and quantity is {quanity}")
