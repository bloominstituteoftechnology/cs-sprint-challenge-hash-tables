#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tester = [
    ticket_1,
    ticket_2,
    ticket_3,
    ticket_4,
    ticket_5,
    ticket_6,
    ticket_7,
    ticket_8,
    ticket_9,
    ticket_10,
]


def reconstruct_trip(tickets, length):
    # build empty hash and result array
    ticket_bag = {}
    route = []

    # shove all the tickets into the hashtable w/source as key and destination as val
    for leg in tickets:
        ticket_bag[leg.source] = leg.destination

    # set the head as the city w/NONE as the source
    departure = ticket_bag["NONE"]

    # loop along the tickets array until we've passed in all the trip-legs
    while len(route) < length:

        # build the arrival
        arrival = ticket_bag[departure]

        # add the leg to the result array
        route.append(departure)

        # set departure to arrival (basically setting current_node as node.next)
        departure = arrival

    return route


print(reconstruct_trip(tester, len(tester)))
