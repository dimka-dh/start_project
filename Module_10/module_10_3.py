import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            summ = randint(50, 500)
            with self.lock:
                self.balance += summ
                print(f'Пополнение: {summ}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            summ = randint(50, 500)
            print(f'Запрос на {summ}')
            with self.lock:
                if summ <= self.balance:
                    self.balance -= summ
                    print(f'Снятие: {summ}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
