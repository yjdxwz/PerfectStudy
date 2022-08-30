import os
a= os.path.split("/user/npb/abc.txt")
print(a)
print(type(a))
b=os.path.splitext('/path/to/file.txt')
print(b)
print(type(b))

c=[x for x in os.listdir('.') if os.path.isdir(x)]
print(c)