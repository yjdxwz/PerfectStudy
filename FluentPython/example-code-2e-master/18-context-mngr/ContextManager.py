from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    print("异常")
    f.close()


with my_open("aaa.py", "w") as f:
    f.write("sdfsdf")
