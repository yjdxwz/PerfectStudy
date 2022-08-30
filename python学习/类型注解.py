from operator import itemgetter
from collections import OrderedDict
from functools import wraps


def ResponseModalTest():
    """
        函数式响应 返回Json数据
    :return:
    """
    resp = OrderedDict()
    resp["name"] = "口碑字符串"
    resp["age"] = 100
    return resp


def getRes(inventory, respons_modal=None):
    countColumns = len(respons_modal.keys())
    keys = list(respons_modal.keys())
    values = list(respons_modal.values())
    listRes = list()
    for entry in inventory:
        res = dict()
        for index in range(countColumns):
            if not entry[index]:
                res[keys[index]] = values[index]
                continue
            res[keys[index]] = entry[index]
        listRes.append(res)
    return listRes


def decrator(*dargs, **dkargs):
    def wrapper(func):
        def _wrapper(*args, **kargs):
            print("装饰器参数:", dargs, dkargs)
            print("函数参数:", args, kargs)
            data = func(*args, **kargs)
            return getRes(data, respons_modal=dkargs.get("respons_modal", None))
        return _wrapper
    return wrapper


@decrator(respons_modal=ResponseModalTest())
def exec():
    inventory = [('', None), ('banana', 2), ('pear', 5), ('orange', 1)]
    return inventory

print(exec())
