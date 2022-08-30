import json

import flask
from concurrent.futures import ProcessPoolExecutor
import math
import time

app = flask.Flask(__name__)


def is_prm(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sort_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sort_n + 1, 2):
        if n % i == 0:
            return False

    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    numbers_list = [int(x) for x in numbers.split(",")]
    result = process_pool.map(is_prm, numbers_list)
    return json.dumps(dict(zip(numbers_list, result)))


if __name__ == '__main__':
    # 定义Pool的 时候 ,保证的条件是 所有的变量都已经声明了
    process_pool = ProcessPoolExecutor()

    app.run()
