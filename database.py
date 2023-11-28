from person import Person
from transport_zone import TransportZone
from bus_route import BusRoute


class Database:
    # Все данные хранятся в словарях,
    # В persons, zones и routes ключами выступают поля id, а значениями - экземпляры,
    # В prices ключ это кортеж из id станции отправления и id станции прибытия, значение - цена билета без багажа
    def __init__(self):
        self.__persons = {}
        self.__zones = {}
        self.__prices = {}
        self.__routes = {}

    def insert_persons(self, persons):
        for person in persons:
            if isinstance(person, Person):
                self.__persons[person.get_id()] = person
            else:
                raise TypeError('Not a Person type!')

    def insert_zones(self, zones):
        for zone in zones:
            if isinstance(zone, TransportZone):
                self.__zones[zone.get_id()] = zone
            else:
                raise TypeError('Not a TransportZone type!')

    def insert_routes(self, rotes):
        for route in rotes:
            if isinstance(route, BusRoute) and \
                    route.get_start_zone() in self.__zones.keys() and \
                    route.get_finish_zone() in self.__zones.keys():
                self.__routes[route.get_id()] = route
            else:
                raise TypeError('Not a BusRoute type!')

    def insert_prices(self, prices):
        for price in prices:
            if isinstance(price, tuple) and \
                    price[0] in self.__zones.keys() and \
                    price[1] in self.__zones.keys() and \
                    isinstance(price[2], int) and \
                    len(price) == 3:
                self.__prices[(price[0], price[1])] = price[2]
            else:
                raise TypeError('Wrong data format!')

    def get_person(self, person_id):
        return self.__persons[person_id]

    def get_zone(self, zone_id):
        return self.__zones[zone_id]

    def get_price(self, start_zone, finish_zone):
        return self.__prices[(start_zone, finish_zone)]

    def get_route(self, route_id):
        return self.__routes[route_id]

    # Метод возвращает id рейса по дате и станциям отправления и прибытия (и в случае наличия мест),
    # либо выбрасывает исключение
    def get_route_id(self, date, start_zone, finish_zone):
        for route in self.__routes.values():
            if route.get_date() == date and \
                    route.get_start_zone() == start_zone and \
                    route.get_finish_zone() == finish_zone and \
                    route.get_capacity() > 0:
                return route.get_id()
        raise RuntimeError('There is no such routes in this date!')

    # Метод для авторизации пользователя в системе
    def authorize(self, login, password):
        for person in self.__persons.values():
            if person.get_login() == login and person.get_hash_pass() == hash(password):
                return person

    def reduce_route_capacity(self, route_id):
        self.__routes[route_id].reduce_capacity()

    def print_routes(self):
        for route in self.__routes.values():
            print(route.get_start_zone(), route.get_finish_zone(), route.get_date(), route.get_capacity())

    def print_tickets(self, user):
        for ticket in user.get_tickets():
            route = self.get_route(ticket.get_route_id())
            print(f'Person: {user.get_fullname()}, Date: {route.get_date()},\n'
                  f'From: {self.get_zone(route.get_start_zone()).get_remark()}, '
                  f'To: {self.get_zone(route.get_finish_zone()).get_remark()},\n'
                  f'Luggage: {"Yes" if ticket.get_luggage() else "No"},\n'
                  f'Place: {ticket.get_place()},\n'
                  f'Price: {ticket.get_price()}\n'
                  f'{30 * "*"}')
