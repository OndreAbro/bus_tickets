# Добавил в класс start_zone, finish_zone, date
class BusRoute:
    def __init__(self, route_id, start_zone, finish_zone, date, capacity, remark):
        self.__id = route_id
        self.__start_zone = start_zone
        self.__finish_zone = finish_zone
        self.__date = date
        self.__remark = remark
        self.__capacity = capacity
        self.__bus_stops = []

    def get_id(self):
        return self.__id

    def get_start_zone(self):
        return self.__start_zone

    def get_finish_zone(self):
        return self.__finish_zone

    def get_date(self):
        return self.__date

    def get_remark(self):
        return self.__remark

    def get_capacity(self):
        return self.__capacity

    def reduce_capacity(self):
        self.__capacity -= 1

    def add_stop(self, bus_stops):
        for bus_stop in bus_stops:
            self.__bus_stops.append(bus_stop)
