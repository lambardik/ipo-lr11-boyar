
from transport.client import Client
from transport.vehicle import Vehicle

class transport_company:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        if vehicle not in self.vehicles:
            self.vehicles.append(vehicle)
        else:
            print("Транспорт уже добавлен")

    def list_vehicles(self):
        return self.vehicles

    def add_client(self, client):
        if client not in self.clients:
            self.clients.append(client)
        else:
            print("Клиент уже добавлен")

    def list_clients(self):
        return self.clients

    def optimize_cargo_distribution(self):
        sorted_clients = sorted(self.clients, key=lambda c: not c.is_vip)

        for vehicle in self.vehicles:
            vehicle.clients_list.clear()
            vehicle.current_load = 0

        for client in sorted_clients:
            for vehicle in self.vehicles:
                try:
                    vehicle.load_cargo(client)
                    print(f"Груз клиента {client.name} загружен в {vehicle}")
                    break
                except ValueError:
                    continue

        print("Распределение грузов завершено.")
