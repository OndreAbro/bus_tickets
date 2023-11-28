from ticket import Ticket


class Person:
    def __init__(self, person_id, fullname, card_number, login, password):
        self.__id = person_id
        self.__fullname = fullname
        self.__card_number = card_number
        self.__login = login
        self.__hash_pass = hash(password)
        self.__tickets = []

    def get_id(self):
        return self.__id

    def get_fullname(self):
        return self.__fullname

    def get_login(self):
        return self.__login

    def set_login(self, login):
        self.__login = login

    def get_hash_pass(self):
        return self.__hash_pass

    def set_hash_pass(self, password):
        self.__hash_pass = hash(password)

    def get_card_number(self):
        return self.__card_number

    def set_card_number(self, card_number):
        self.__card_number = card_number

    def get_tickets(self):
        return self.__tickets

    # При покупке билета сперва ищем его в базе данных по дате и станциям отправления и прибытия,
    # затем также в базе данных ищем цену билета, корректируем ее с учетом багажа, производим оплату
    # и сохраняем созданный билет в списке билетов юзера.
    def buy_ticket(self, date, start_zone, finish_zone, place, luggage, db):
        route_id = db.get_route_id(date, start_zone, finish_zone)
        db.reduce_route_capacity(route_id)
        price = db.get_price(start_zone, finish_zone)
        price = round(price * 1.1, 2) if luggage else price
        self.get_payment(price)
        self.__tickets.append(Ticket(luggage, place, route_id, price))

    def get_payment(self, price):
        pass

