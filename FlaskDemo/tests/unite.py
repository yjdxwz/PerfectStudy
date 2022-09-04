import unittest


class Testcase(unittest.TestCase):

    def setUp(self) -> None:
        print("执行setUp")

    def test_1(self):
        print("执行第一个")

    def test_2(self):
        print("第二个")

    def test_3(self):
        print("第三个")

    def test_10(self):
        print("第四个")

    def test_11(self):
        print("第五个")

    def tearDown(self) -> None:
        print("执行 tearDown")


if __name__ == "__main__":
    unittest.main()