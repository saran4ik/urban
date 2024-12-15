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
            self.balance += rep
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"#{i} Пополнение: {rep}. Баланс: {self.balance} \n", end='')
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdrawal = randint(50, 500)
            print(f"#{i} Запрос на {withdrawal} \n", end='')
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f"Снятие: {withdrawal}. Баланс: {self.balance} \n", end='')
            else:
                print("Запрос отклонён, недостаточно средств \n", end='')  
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
