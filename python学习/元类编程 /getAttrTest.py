from datetime import date, datetime


class User():
    def __init__(self, name, birthday, info=None):
        self.name = name
        self.birthday = birthday
        self.info = info
        # self._age = 0

    # 查找不到 属性的时候 ， 才会进入这里
    def __getattr__(self, item):
        return self.info[item]

    # 访问所有属性
    def __getattribute__(self, item):
        return "boboy "


if __name__ == '__main__':
    user = User("bobby", date(year=1987, month=1, day=1), info={"company_name": "jjjj"})
    # user.age = 90
    # print(user.age)
    print(user.company_name)
