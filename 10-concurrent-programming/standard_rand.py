from concurrent.futures import (
    ProcessPoolExecutor,
    as_completed
)
import random

def use_starndard_random():
    return random.random()

def main():
    with ProcessPoolExecutor() as e:
        futures = [e.submit(use_starndard_random)
                   for _ in range(3)]
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()