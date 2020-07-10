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
    for t in tickets:
        cache[t.source] = t.destination

    destination = cache['NONE']

    for flight in range(length):
        route[flight] = destination
        destination = cache[destination]

    return route