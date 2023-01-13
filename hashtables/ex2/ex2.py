#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    locate = {ticket.source: ticket.destination for ticket in tickets}
    location = locate["NONE"]
    route = [location]

    while location is not "NONE":
        location = locate[location]
        route.append(location)

    return route
