class A():
    def __init__(self, key):
        self.a = key


class B():
    a = None

    # self.a 是可以直接用的
    def __init__(self, key):
        self.b = key

    def getLog(self):
        print("A.log", self.a)


class C():
    def __init__(self, key):
        self.c = key


class D(A, B, C):

    def __init__(self, key):
        A.__init__(self, key)
        print("log")
        B.__init__(self, key)
        self.getLog()
        C.__init__(self, key)
        self.d = key


class E(D):
    def __init__(self, key):
        D.__init__(self, key)

        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
        self.actions()

    def actions(self):
        print("结束了")


instance = D("aaaa")

print(instance.a)
print(instance.b)
print(instance.c)
print(instance.d)

E("bbbbbb")

# /usr/bin/python3 /Users/root1/opt/project/backend/lhq/python学习/面向对象/test001.py
# aaaa
# aaaa
# aaaa
# aaaa
# bbbbbb
# bbbbbb
# bbbbbb
# bbbbbb

