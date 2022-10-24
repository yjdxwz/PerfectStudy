import traceback


def func(num1, num2):
    try:
        x = num1 * num2
        y = num1 / num2
        return x, y
    except:
        traceback.print_exc(file=open('YFater.txt', 'w+'))


func(1, 0)


import stat

import wtforms

type("s")


class A(object):
    def __call__(self, *args, **kwargs):
        pass