from datetime import date, datetime


class User():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    # 计算属性 ， 可以当一个属性进行调用 ， 原先的是函数， 现在的是 属性
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    # 动态属性 赋值操作
    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User("bobby", date(year=1987, month=1, day=1))
    user.age = 90
    print(user.age)
    print(user._age)
# 35
# 90