import json
import sys
import unittest
from io import StringIO
from unittest.mock import patch, MagicMock


class BuildUrlTest(unittest.TestCase):
    def test_build_url(self):
        # build_url()이 테스트 대상 처리
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?q=python'
        actual = build_url({'q': 'python'})
        # assert 메서드 이용
        self.assertEqual(expected, actual)

    def test_build_url_empty_param(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?'
        actual = build_url({})
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_build_url_fail(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes'
        actual = build_url({})
        self.assertEqual(expected, actual,
                         msg='이 테스트는 실패합니다')

    # 인수로 테스트를 건너 뛰는 이유를 전달
    @unittest.skip('this is a skip test')
    def test_nothing_skip(self):
        pass

    # 실행 중인 파이썬 버전이 3.6보다 높으면 건너뜀
    @unittest.skipIf(sys.version_info > (3, 6),
                     'this is a skipIf test')
    def test_nothing_skipIf(self):
        pass


class BuildUrlMultiTest(unittest.TestCase):
    def test_build_url_multi(self):
        from booksearch.api import build_url
        base = 'https://www.googleapis.com/books/v1/volumes?'
        expected_url = f'{base}q=python'
        # 2번째, 3번째 테스트는 실패함
        params = (
            (expected_url, {'q': 'python'}),
            (expected_url, {'q': 'python', 'maxResults': 1}),
            (expected_url, {'q': 'python', 'langRestrict': 'en'}),
        )
        for expected, param in params:
            with self.subTest(**param):
                actual = build_url(param)
                self.assertEqual(expected, actual)


class GetJsonTest(unittest.TestCase):
    def test_get_json(self):
        from booksearch.api import get_json
        with patch('booksearch.api.request.urlopen') as mock_urlopen:
            # 컨텍스트 관리자의 목(mock)을 준비
            # API 응답이 될 JSON 데이터 준비
            expected_response = {'id': 'test'}
            fp = StringIO(json.dumps(expected_response))

            # MagicMock 클래스를 사용하면 __exit__를 추가할 필요 없음
            mock = MagicMock()
            mock.__enter__.return_value = fp
            # urlopen()의 반환값이 컨텍스트 관리자
            mock_urlopen.return_value = mock
            actual = get_json({'q': 'python'})
            self.assertEqual(expected_response, actual)
