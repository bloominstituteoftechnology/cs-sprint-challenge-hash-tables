#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    route = [None] * length

    # add tickets to cache
    for ticket in tickets:
        # source is key, destination is value
        cache[ticket.source] = ticket.destination

    # destination first flight
    destination = cache['NONE']

    for flight in range(length):
        # save destination to route
        route[flight] = destination
        # find next destination
        destination = cache[destination]

    return route
