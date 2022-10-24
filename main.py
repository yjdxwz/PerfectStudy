# def a(aaa:int)-> int:
#     return  aaa*2
#
# print(a(11))
#
#
# with open("","") as f:



#     f.read()



class WithContextCustom(object):

    def __init__(self,name):
        self.name = name


    def __enter__(self):
        print(f"{self.name}进来了")
        return  "ABC"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name}退出了")
        try:
            1/0
        except Exception as e:
            print(exc_type, exc_val, exc_tb)





with WithContextCustom("xxxx"):
    print("xxxddd")

# print(f)