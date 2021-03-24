# unittest 모듈을 로딩해서 이용함
import unittest


class TestFunc(unittest.TestCase):
    def test_func(self):
        from hello import func
        self.assertIsNone(func('안녕하세요'))
