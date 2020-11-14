#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = [None] * length
    cache = {}

    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    next = cache["NONE"]

    for current in range(0, length):
        route[current] = next
        next = cache[next]
    return route
