#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tixlist, length):
    flights = {}
    for tick in tixlist:
        flights[tick.source] = tick.destination
    route = []
    val = flights['NONE']
    while val != 'NONE':
        route.append(val)
        val = flights[val]
    route.append(val)
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, len(tickets))