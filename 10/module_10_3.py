import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rep = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += rep
            print(f"#{i} Пополнение: {rep}. Баланс: {self.balance}", flush=True)
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdrawal = randint(50, 500)
            print(f"#{i} Запрос на {withdrawal}", flush=True)
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f"Снятие: {withdrawal}. Баланс: {self.balance}", flush=True)
            else:
                print("Запрос отклонён, недостаточно средств", flush=True)
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
