#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    route = []
    route.append(cache["NONE"])

    for ticket in tickets:
        _next = route[-1]
        route.append(cache[_next])
        if route[-1] == "NONE":
            return route
