#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    lookup = {ticket.source: ticket.destination for ticket in tickets}
    location = lookup["NONE"]
    route = [location]

    while location != "NONE":
        location = lookup[location]
        route.append(location)
    return route
