class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = int(phone)

    
    def __str__(self):
        return f"Hi! {self.name} , my phone number is {self.phone}"
    

    def greet(self):
        print(self.name , "  ---  ", self.phone)




p1 = Person("raj", 93830)


print(p1.name)
print(p1.phone)

print(p1)

# print(str(p1))