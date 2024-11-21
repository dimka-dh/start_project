import time
from threading import Thread
from datetime import timedelta


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time.time()
times_run = timedelta(seconds=end_time - start_time)
print(f"Работа функций {times_run}")

start_time = time.time()
threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt")),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
times_run = timedelta(seconds=end_time - start_time)
print(f"Работа потоков {times_run}")