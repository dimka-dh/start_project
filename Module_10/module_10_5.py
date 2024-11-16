import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print("Линейный:", time.time() - start_time)

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print("Многопроцессный:", time.time() - start_time)
