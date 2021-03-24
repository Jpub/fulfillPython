from typing import Optional


def increment(page_num: int,
              last: int,
              *,
              ignore_error: bool = False) -> Optional[int]:
    """다음 페이지 번호를 반환함

    :param page_num: 원래 페이지 번호
    :param last: 마지막 페잊 번호
    :param ignore_error: True이면 페이지를 벗어났을 때도 예외를 발생시키지 않음
    :return: 다음 페이지 번호
    """
    next_page = page_num + 1
    if next_page <= last:
        return next_page
    if ignore_error:
        return None
    raise ValueError("Invalid arguments")


# 타입이 일치하지 않는 호출
increment(1, 10, ignore_error=1)
