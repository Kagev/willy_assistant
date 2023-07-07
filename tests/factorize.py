import time
from multiprocessing import cpu_count, Pool


def factorize(number):
    factors = []
    for num in number:
        factors.append([])
        for i in range(1, num + 1):
            if num % i == 0:
                factors[-1].append(i)
    return factors


def parallel_factorize(*numbers):
    pool = Pool(processes=cpu_count())
    result = pool.map(factorize, [numbers])
    pool.close()
    pool.join()
    return result[0]


if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize([128, 255, 99999, 10651060])
    end_time = time.time()
    print("Results factorize - SYNC")
    print("Lead time (sync vers): ", end_time - start_time, "s")

    start_time = time.time()
    a, b, c, d = parallel_factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    print("Results factorize - PARA")
    print("Lead time (parallel vers): ", end_time - start_time, "s")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]
