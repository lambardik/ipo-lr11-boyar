import random
from transport.client import Client

class Vehicle:
    vehicle_counter = 1

    def __init__(self, capacity, current_load=0):
        self.vehicle_id = str(random.randint(1000, 100000))
        try:
            capacity = int(capacity)
        except ValueError:
            raise ValueError("Грузоподъемность указывается числом")
        Vehicle.vehicle_counter += 1
        self.capacity = capacity
        self.clients_list = []
        self.current_load = 0

    def load_cargo(self, client):
        try:
            new_weight = self.current_load + client.cargo_weight
        except AttributeError:
            raise AttributeError("Вы должны передать клиента в параметр функции!")
        if new_weight > self.capacity:
            print("Грузоподъемность превышена! Действие отменено!")
        else:
            self.current_load = new_weight
            self.clients_list.append(client)

    def __str__(self):
        return f"ID транспорта: {self.vehicle_id}\nГрузоподъемность транспорта: {self.capacity}\nЗагружено: {self.current_load}"