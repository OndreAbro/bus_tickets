from person import Person
from transport_zone import TransportZone
from ticket import Ticket
from bus_route import BusRoute
from database import Database
from datetime import date


db = Database()

db.insert_persons([Person(1, 'Ivanov I.I.', 1111, 'login_1', '123'), Person(2, 'Petrov P.P.', 2222, 'login_2', '222')])

db.insert_zones([TransportZone(1, 'Moscow'), TransportZone(2, 'Kazan'), TransportZone(3, 'Pskov')])

db.insert_routes([BusRoute(1, 1, 2, date(2023, 11, 28), 30, 'from Moscow to Kazan'),
                  BusRoute(2, 1, 2, date(2023, 11, 30), 30, 'from Moscow to Kazan'),
                  BusRoute(3, 1, 3, date(2023, 11, 30), 35, 'from Moscow to Pskov'),
                  BusRoute(4, 1, 3, date(2023, 12, 1), 40, 'from Moscow to Pskov'),
                  BusRoute(5, 2, 1, date(2023, 11, 29), 30, 'from Kazan to Moscow'),
                  BusRoute(6, 3, 1, date(2023, 12, 2), 35, 'from Pskov to Moscow')])

db.insert_prices([(1, 2, 2000), (1, 3, 1600), (2, 1, 1900), (3, 1, 1500)])

user_1 = db.authorize('login_1', '123')
user_2 = db.authorize('login_2', '222')

user_1.buy_ticket(date(2023, 11, 30), 1, 2, 27, True, db)

user_2.buy_ticket(date(2023, 11, 29), 2, 1, 10, False, db)
user_2.buy_ticket(date(2023, 12, 2), 3, 1, 33, True, db)

db.print_tickets(user_1)
db.print_tickets(user_2)


