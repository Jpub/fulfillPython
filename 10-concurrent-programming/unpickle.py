from concurrent.futures import (
    ProcessPoolExecutor,
    wait
)

func = lambda: 1

def main():
    with ProcessPoolExecutor() as e:
        future = e.submit(func)
        done, _ = wait([future])
    print(future.result())

if __name__ == '__main__':
    main()