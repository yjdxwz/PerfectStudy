with open("ContextManager.py") as fp:
    src = fp.read(60)

print(src)
print(len(src))
print(src)
# print("*".center(src))
print(fp)
print(fp.closed,fp.encoding)

print(fp.read(30))

from _io import TextIOWrapper

