import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

# 기본값이 INFO 레벨이므로, DEBUG 레벨 로그는 무시됨
logger.setLevel(logging.INFO)

@contextmanager
def debug_context():
    level = logger.level
    try:
        # 로깅 레벨을 변경함
        logger.setLevel(logging.DEBUG)
        yield
    finally:
        # 원래 로깅 레벨로 되돌림
        logger.setLevel(level)

def main():
    logger.info('before: info log')
    logger.debug('before: debug log')

    # DEBUG 로그를 볼 때의 처리를 with 문 블록 안에서 실행함
    with debug_context():
        logger.info('inside the block: info log')
        logger.debug('inside the block: debug log')

    logger.info('after: info log')
    logger.debug('after: debug log')

if __name__ == '__main__':
    main()