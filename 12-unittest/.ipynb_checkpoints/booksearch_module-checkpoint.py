import unittest

# 애플리케이션 코드
def booksearch():
    # 임의 처리
    return {}

class BookSearchTest(unittest.TestCase):
    # booksearch() 테스트 코드
    def test_booksearch(self):
        self.assertEqual({}, booksearch())


if __name__ == '__main__':
    unittest.main()