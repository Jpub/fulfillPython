import json
import sys
import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

class BuildUrlTest(unittest.TestCase):
    def test_build_url(self):
        # build_url()がテスト対象の処理
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?q=python'
        actual = build_url({'q': 'python'})
        # アサーションメソッドの利用
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
                         msg='このテストは失敗します')

    # 引数にスキップする理由を渡す
    @unittest.skip('this is a skip test')
    def test_nothing_skip(self):
        pass
    
    # 実行中のPythonバージョンが3.6より大きければスキップ
    @unittest.skipIf(sys.version_info > (3, 6),
                     'this is a skipIf test')
    def test_nothing_skipIf(self):
        pass


class BuildUrlMultiTest(unittest.TestCase):
    def test_build_url_multi(self):
        from booksearch.api import build_url
        base = 'https://www.googleapis.com/books/v1/volumes?'
        expected_url = f'{base}q=python'
        # 2番目、3番目のテストは失敗する
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
            # コンテキストマネージャーのモックを用意
            # APIレスポンスになるJSONデータを用意する
            expected_response = {'id': 'test'}
            fp = StringIO(json.dumps(expected_response))

            # MagicMockクラスを使うと__exit__の追加は不要
            mock = MagicMock()
            mock.__enter__.return_value = fp
            # urlopen()の戻り値がコンテキストマネージャー
            mock_urlopen.return_value = mock
            actual = get_json({'q': 'python'})
            self.assertEqual(expected_response, actual)