# Часть полей перенес в BusRoute
class Ticket:
    def __init__(self, luggage, place, route_id, price):
        self.__luggage = luggage
        self.__place = place
        self.__route_id = route_id
        self.__price = price

    def get_route_id(self):
        return self.__route_id

    def get_luggage(self):
        return self.__luggage

    def get_place(self):
        return self.__place

    def get_price(self):
        return self.__price