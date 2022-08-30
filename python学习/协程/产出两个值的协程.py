def simple_coro2(a):
    print("start: a = ",a)
    b = yield a
    print("recevied b = ",b)
    c = yield a + b
    print("recevied c = ",c )

