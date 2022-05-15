import pickle


class Autobus:
    def __init__(self, number, start_point, end_point, time):
        self.number = number
        self.start_point = start_point
        self.end_point = end_point
        self.time = time

    def info(self):
        print("-" * 20)
        print(f'Route number is: {self.number}')
        print(f'Starting point: {self.start_point}')
        print(f'Destination point: {self.end_point}')
        print(f'Travel time: {self.time}')
        print("-" * 20)

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_start_point(self):
        return self.start_point

    def set_start_point(self, start_point):
        self.start_point = start_point

    def get_end_point(self):
        return self.end_point

    def set_end_point(self, end_point):
        self.end_point = end_point

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time


# bus = Autobus(422, "Lviv", "Kyiv", "11:15")
# bus.info()
# bus.set_number(244)
# bus.get_number()


def create_autopark():
    autopark = list()
    num_of_auto = int(input("Write number of buses: "))
    for i in range(num_of_auto):
        route_number = int(input(f"Enter the route number of {i + 1} bus: "))
        starting_point = input(f"Enter the starting point of {i + 1} bus: ")
        destination_point = input(f"Enter the destination point of {i + 1} bus: ")
        travel_time = input(f"Enter the travel time of {i + 1} bus: ")
        autopark.append(Autobus(route_number, starting_point, destination_point, travel_time))
    with open("autopark.bin", "wb") as file:
        pickle.dump(autopark, file)
    # return autopark


def show_autopark():
    with open("autopark.bin", "rb") as file:
        buses = pickle.load(file)
    for i in buses:
        i.info()


def sort_by_number():
    with open("autopark.bin", "rb") as file:
        buses = pickle.load(file)
    for b in list(sorted(buses, key=lambda x: x.number, reverse=True)):
        b.info()


def search_by_point(point):
    with open("autopark.bin", "rb") as file:
        buses = pickle.load(file)
    for i in buses:
        if point == i.get_start_point() or point == i.get_end_point():
            i.info()
