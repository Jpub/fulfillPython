import imghdr
import pathlib
from .api import get_data, get_json


class Book:
    """API 응답의 VolumeInfo 엘리먼트에 대응"""

    def __init__(self, item):
        self.id = item['id']
        volume_info = item['volumeInfo']
        for k, v in volume_info.items():
            setattr(self, str(k), v)

    def __repr__(self):
        return str(self.__dict__)

    def save_thumbnails(self, prefix):
        """섬네일 이미지를 저장함"""
        paths = []
        for kind, url in self.imageLinks.items():
            thumbnail = get_data(url)
            # 이미지 데이터로부터 확장자 판정
            ext = imghdr.what(None, h=thumbnail)
            # pathlib.Path는 / 연산자로 경로를 추가할 수 있음
            base = pathlib.Path(
                prefix) / f'{self.id}_{kind}'
            filename = base.with_suffix(f'.{ext}')
            filename.write_bytes(thumbnail)
            paths.append(filename)
        return paths


def get_books(q, **params):
    """서적 검색 수행"""
    params['q'] = q
    data = get_json(params)
    return [Book(item) for item in data['items']]
