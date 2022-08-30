import os

currentPath = os.getcwd()
#  打印 制定路径下所有文件名
path = os.listdir(currentPath)


def getDirPath(path):
    pathList = os.listdir(path)
    for file in pathList:
        sunCurrentPath = os.path.join(path, file)

        if os.path.isdir(sunCurrentPath):

            getDirPath(sunCurrentPath)
        else:
            print(os.path.join(path, sunCurrentPath))


getDirPath(currentPath)
