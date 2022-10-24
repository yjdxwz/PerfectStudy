import numbers

class Group:
    # 支持切片操作

    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        """实现切片的关键 """
        return self.staffs[item]

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        """ 可迭代 """
        return iter(self.staffs)

    def __contains__(self, item):
        """
            if  in  实现的 是 contains 函数
        :param item:
        :return:
        """
        if item in self.staffs:
            return True
        return False




staffs = ["boby","imooc", "boby1"]
group = Group(company_name="imooc" , group_name="user",staffs=staffs)


a = group[:2]

if "boby" in group:
    print("yes")
reversed(group)

for user in group:
    print(user)