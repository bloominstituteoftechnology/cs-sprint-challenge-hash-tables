#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route_dict = {}

    route = [None] * length

    for ticket in tickets:
        route_dict[ticket.source] = ticket.destination
    next_stop = route_dict["NONE"]

    for r in range(0, length):
        route[r] = next_stop
        next_stop = route_dict[next_stop]

    return route
