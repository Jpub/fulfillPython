from concurrent.futures import (
    ProcessPoolExecutor,
    as_completed
)
import numpy as np

def use_numpy_random():
    # 난수 생성기를 초기화할 때 이 행을 실행함
    # np.random.seed()
    return np.random.random()

def main():
    with ProcessPoolExecutor() as e:
        futures = [e.submit(use_numpy_random)
                   for _ in range(3)]
        for future in as_completed(futures):
            print(future.result())

if __name__ == '__main__':
    main()