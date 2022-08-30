from autoTest.metaClass.atomic_func import WebDriver
import os


# 需要更改类名 aaa
class aaa(WebDriver):
    def __init__(self, filePath):
        super().__init__(filePath)

    # 可变方法
    def getAllData(self, **kwargs):
        """
            这个方法是 yml 文件 execApi 执行的方法
        :param kwargs:
        :return:
        """
        print(kwargs)


if __name__ == '__main__':
    filePath = os.path.abspath('.')
    obj = aaa(filePath)  # 需要更改
    obj.start()
