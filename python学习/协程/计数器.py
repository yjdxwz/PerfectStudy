# 生成器计算平均值
def sum_coroutine():
    total = 0.0
    count = 0
    average = None

    while True:
        item =yield average
        total +=item
        count +=1
        average = total/count

# aaa = sum_coroutine()
# next(aaa)
# aaa.send(40)
# 40.0
# aaa.send(20)
# 30.0
# aaa.send(20)
# 26.666666666666668
