import pathlib
import unittest
from unittest.mock import patch
from urllib.error import URLError
from tempfile import TemporaryDirectory

THUMBNAIL_URL = (
    'http://books.google.com/books/content'
    '?id=OgtBw76OY5EC&printsec=frontcover'
    '&img=1&zoom=1&edge=curl&source=gbs_api'
)


class SaveThumbnailsTest(unittest.TestCase):
    def setUp(self):
        # 임시 디렉터리 작성
        self.tmp = TemporaryDirectory()

    def tearDown(self):
        # 임시 디렉터리 정리
        self.tmp.cleanup()

    def test_save_thumbnails(self):
        from booksearch.core import Book
        book = Book({'id': '', 'volumeInfo': {
            'imageLinks': {
                'thumbnail': THUMBNAIL_URL
            }}})
        # 처리를 실행하고 파일이 작성되었음을 확인
        filename = book.save_thumbnails(self.tmp.name)[0]
        self.assertTrue(pathlib.Path(filename).exists())

    # 테스트 대상의 save_thumbnail()가 이용할 참조 이름을 지정
    @patch('booksearch.core.get_data')
    def test_save_thumbnails(self, mock_get_data):
        from booksearch.core import Book

        # 앞에서 얻은 섬네일 이미지 데이터를 목의 반환값으로 설정
        data_path = pathlib.Path(__file__).with_name('data')
        with open(data_path / 'YkGmfbil6L4C_thumbnail.jpeg', 'rb') as f:
            data = f.read()
        mock_get_data.return_value = data

        book = Book({'id': '', 'volumeInfo': {
            'imageLinks': {
                'thumbnail': THUMBNAIL_URL
            }}})
        filename = book.save_thumbnails(self.tmp.name)[0]

        # get_data() 호출 시의 인수 확인
        mock_get_data.assert_called_with(THUMBNAIL_URL)

        # 저장된 데이터 확인
        with open(filename, 'rb') as f:
            self.assertEqual(data, f.read())


class GetBooksTest(unittest.TestCase):
    def test_get_books_no_connection(self):
        from booksearch.core import get_books

        # 임시로 네트워크 접속 단절
        with patch('socket.socket.connect') as mock:
            # connect()가 호출되면 정확하지 않은 값을 반환함
            mock.return_value = None
            with self.assertRaisesRegex(URLError, 'urlopen error'):
                # 예외가 발생하는 처리를 with 블록 안에서 실행
                get_books(q='python')
