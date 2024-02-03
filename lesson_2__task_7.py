""" Урок 2, завдання 7
Створіть ієрархію класів транспортних засобів. У загальному класі опишіть загальні для всіх транспортних
засобів поля, у спадкоємцях – специфічні їм. Створіть кілька екземплярів. Виведіть інформацію щодо
кожного транспортного засобу.
"""


class Vehicle:
    def __init__(self, brand, model, year, color, max_speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.max_speed = max_speed

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.color}, ' \
               f'Max speed: {self.max_speed}'


class Car(Vehicle):
    def __init__(self, brand, model, year, color, max_speed, num_doors=4, num_seats=5):
        super().__init__(brand, model, year, color, max_speed)
        self.num_doors = num_doors
        self.num_seats = num_seats

    def __str__(self):
        return f'{super().__str__()}, Number of doors: {self.num_doors}, Number of seats: {self.num_seats}'


class Bus(Vehicle):
    def __init__(self, brand, model, year, color, max_speed, num_seats, bus_line):
        super().__init__(brand, model, year, color, max_speed)
        self.num_seats = num_seats
        self.bus_line = bus_line

    def __str__(self):
        return f'{super().__str__()}, Number of seats: {self.num_seats}, Bus line: {self.bus_line}'


class Truck(Vehicle):
    def __init__(self, brand, model, year, color, max_speed=100, fuel_type='diesel'):
        super().__init__(brand, model, year, color, max_speed)
        self.fuel_type = fuel_type

    def __str__(self):
        return f'{super().__str__()}, Fuel type: {self.fuel_type}'


class Refrigerated(Truck):
    def __init__(self, brand, model, year, color, max_load, max_speed=150, fuel_type='electric',
                 lowest_temperature=-18):
        super().__init__(brand, model, year, color, max_speed, fuel_type)
        self.max_load = max_load
        self.low_temp = lowest_temperature

    def __str__(self):
        return f'{super().__str__()}, Loading capacity: {self.max_load}, Lowest temperature: {self.low_temp}'


class Tanker(Truck):
    def __init__(self, brand, model, year, color, max_capacity):
        super().__init__(brand, model, year, color)
        self.max_capacity = max_capacity

    def __str__(self):
        return f'{super().__str__()}, Maximum capacity: {self.max_capacity}'


car = Car('Toyota', 'Camry', 2020, 'Red', 200)
bus = Bus('Volvo', 'Bus', 2019, 'White', 50, 50, '1')
refrigerated = Refrigerated('Tesla', 'Refrigerated', 2022, 'Blue', 10000, 120, lowest_temperature=-20)
tanker = Tanker('Volvo', 'Tanker', 2022, 'Green', 100000)

print(type(car), car)
print(type(bus), bus)
print(type(refrigerated), refrigerated)
print(type(tanker), tanker)
