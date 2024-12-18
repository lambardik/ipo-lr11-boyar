from transport.van import Van
from transport.vehicle import Vehicle
from transport.client import Client
from transport.ship import Ship
from transport.transport_company import transport_company

def main():
    company = transport_company("Компания")

    while True:
        print("\nМеню:")
        print("1. Добавить клиента")
        print("2. Добавить фургон")
        print("3. Добавить судно")
        print("4. Распределить грузы")
        print("5. Показать транспорт и загрузку")
        print("6. Вывести всех клиентов")
        print("7. Вывести весь транспорт")
        print("8. Выйти")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            try:
                name = input("Введите имя клиента: ")
                weight = float(input("Введите вес груза (кг): "))
                is_vip_input = input("Клиент VIP? (да/нет): ").strip().lower()
                is_vip = is_vip_input == "да"

                client = Client(name, weight, is_vip)
                company.add_client(client)
                print("Клиент добавлен.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            try:
                capacity = int(input("Введите грузоподъемность фургона (т): "))
                if capacity <= 0:
                    raise ValueError("Грузоподъемность должна быть положительной.")
                is_refrigerated_input = input("Введите есть ли холодильник (да/нет): ").strip().lower()
                is_refrigerated = is_refrigerated_input == 'да'
                vehicle = Van(capacity, is_refrigerated)
                company.add_vehicle(vehicle)
                print("Фургон добавлен.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            try:
                capacity = int(input("Введите грузоподъемность судна (т): "))
                if capacity <= 0:
                    raise ValueError("Грузоподъемность должна быть положительной.")
                name_input = input("Введите название судна: ")
                name = name_input
                vehicle = Ship(capacity, name)
                company.add_vehicle(vehicle)
                print("Судно добавлено.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            company.optimize_cargo_distribution()
            print("Грузы распределены.")

        elif choice == "5":
            for vehicle in company.list_vehicles():
                print(vehicle)
                for client in vehicle.clients_list:
                    print(f"  - {client}")

        elif choice == "6":
            for client in company.list_clients():
                print(client)

        elif choice == "7":
            for vehicle in company.list_vehicles():
                print(vehicle)

        elif choice == "8":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()