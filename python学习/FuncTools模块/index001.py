from functools import lru_cache

# 指定最大缓存数量
# maxsize None , 没有限制
# typed:True 不同类型参数分别缓存 f(3) f(3.0)
# 被装饰的 函数可以调用 cache_parameter(): 返回的是一个字典类型, 包含他所在的装饰器参数
# case_clear()清理缓存
# 最近最少使用算法, 根据历史访问记录 来进行淘汰数据
# 近期访问过, 未来访问几率更高
@lru_cache(maxsize=100,typed=False)
def factorial(n):
    return n*factorial(n-1) if n else 1
