a= 1
b=4


a, b = b, a
print(a,b)
list = []

# [{"num":0}]

#  字典是可变类型 , 修改后变量不用重新赋值
# 也就是说所有内存里面的a 这个变量对于字典都会改变
a= {"num":1}
for line in range(3):

    a["num"]=line
    list.append(a)
print(list)
# [{'num': 2}, {'num': 2}, {'num': 2}]


import copy
li = []
a={"num":1}
for line in range(3):
    b = copy.deepcopy(a)
    b["num"]=line
    li.append(b)

print(li)
