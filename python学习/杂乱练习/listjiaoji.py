set1 = {2,2.2,True,4+3j}
set2 = {1,2.2,False,4+3j,7}
#  求交集
print(set1& set2)
print(set2& set1)
print(int(True))
# {True, 2.2, (4+3j)}
# {True, 2.2, (4+3j)}
# 1

#  求并集
print(set1|set2)
# {False, True, 2, 2.2, (4+3j)}

# 交集以 右侧为准
# 并集以 左侧为准



print(set1 -set2)