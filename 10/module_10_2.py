from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.power = power
        self.name = name

    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!\n', end='')
        while enemies > 0:
            days += 1
            enemies -= self.power
            if enemies < self.power:
                print(f"{self.name} одержал победу спустя {days} дней!\n", end='')
            else:
                print(f"{self.name} сражается {days} день(ей)..., осталось {enemies} воинов.\n", end='')
                sleep(1)



first_knight = Knight('Sir Lancelot', 11)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
sleep(0.1)
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
