import bisect

# 用来处理已排序的序列， 用来维持已排序的序列 ， 升序
inter_list = list()
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)


print(bisect.bisect(inter_list, 000))