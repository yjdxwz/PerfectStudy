class openFile():
    def __init__(self, fileName, mode):
        self.fileName = fileName
        self.mode = mode

    def __enter__(self):
        print("进入 enter 方法")
        self.f = open(self.fileName, mode=self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        self.f.close()
    # def __exit__(self, exc_type, exc_val, exc_tb):


def m4():
    with openFile("aaa.py", 'w') as f:
        f.write("123")
        f.write("456")


m4()
