
import random
from .client import Client

class Vehicle:
    def __init__(self, capacity, current_load=0):
        self.vehicle_id = str(random.randint(1000, 100000))
        try:
            capacity = int(capacity)
        except ValueError:
            raise ValueError("Грузоподъемность указана некорректно.")
        try:
            current_load = int(current_load)
        except ValueError:
            raise ValueError("Текущая загрузка указана некорректно.")
        self.capacity = capacity
        self.clients_list = []
        self.current_load = current_load

    def load_cargo(self, client):
        try:
            new_weight = self.current_load + client.cargo_weight
        except AttributeError:
            raise AttributeError("Необходимо передать клиента в параметр функции.")
        if new_weight > self.capacity:
            print("Грузоподъемность превышена!")
        else:
            self.current_load = new_weight
            self.clients_list.append(client)

    def __str__(self):
        return f"ID транспорта: {self.vehicle_id}\nГрузоподъемность транспорта: {self.capacity}\nЗагружено: {self.current_load}"
