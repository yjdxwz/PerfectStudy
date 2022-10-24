
import traceback

class MyType(type):
    def __init__(self, *args, **kwargs):
        print("MyType __init__")
        super().__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        print("MyType __new__")
        new_cls = super().__new__(cls, *args, **kwargs)
        return new_cls

    def __call__(self, *args, **kwargs):
        print("MyType __call__")
        new_obj = self.__new__(self )
        self.__init__(new_obj, *args, **kwargs)
        return new_obj


# class Foo(object):
class Foo(object, metaclass=MyType):
    def __new__(cls, *args, **kwargs):
        print("Foo __new__")
        new_cls = super().__new__(cls, *args, **kwargs)
        return new_cls

    def __init__(self,name):
        print("Foo __init__")
        self.name = name

    def __call__(self, *args, **kwargs):
        print("Foo __call__")


# MyType __new__
# MyType __init__

#
#
a=Foo("sss")
# # MyType __call__
# # Foo __new__
# # Foo __init__
#
#
# try:
#     a()
# except TypeError:
#     print(traceback.format_exc(),"xx")
# except Exception as e:
#     print(traceback.format_exc())
