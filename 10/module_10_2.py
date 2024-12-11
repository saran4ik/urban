from threading import Thread, Lock
from time import sleep
Lock = Lock()


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.power = power
        self.name = name

    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while enemies > 0:
            #Lock.acquire()
            days += 1
            enemies -= self.power
            print(f"{self.name} сражается {days} день(ей)..., осталось {enemies} воинов.")
            sleep(1)
            #sleep(self.power/10)
            #sleep(10/self.power)
            #Lock.release()
        print(f"{self.name} одержал победу спустя {days} дней!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
sleep(0.1)
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
