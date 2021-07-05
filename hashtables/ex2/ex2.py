#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length, cache={}):
    route = [None] * length
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    # Set next location to the DESTINATION of the starting point.
    nextLocation = cache["NONE"]
    for index in range(0, length):
        route[index] = nextLocation
        # Set the next location to the VALUE of the current airport, which is the next one.
        nextLocation = cache[nextLocation]
    return route
