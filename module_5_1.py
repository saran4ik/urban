class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if int(new_floor) not in range(1, int(self.number_of_floors) + 1):
            print("Такого этажа не существует")
        else:
            print(*[i for i in range(1, int(new_floor) + 1)], sep="\n")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ПГТ Шиханы', 5)
h1.go_to(5)
h2.go_to(10)
h3.go_to(5)