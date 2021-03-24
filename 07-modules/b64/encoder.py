import base64
import sys


def str_to_base64(x):
    """문자열을 base64 표현으로 변환함

    b64encode()는 bytes-like objec를 인수로 받으므로
    문자열은 encode()로 bytes 타입으로 전달함
    """
    return base64.b64encode(x.encode('utf-8'))


def main():
    target = sys.argv[1]
    print(str_to_base64(target))


if __name__ == '__main__':
    main()

__all__ = ['str_to_base64']
