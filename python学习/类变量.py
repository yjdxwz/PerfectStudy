class Person:
    name = "aaa"


p1 = Person()
p2 = Person()
p1.name = "bbb"
print(p1.name)  # bbb
print(p2.name)  # bbb
print(Person.name)  # aaa
