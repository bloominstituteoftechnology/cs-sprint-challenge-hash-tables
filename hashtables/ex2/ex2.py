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
    route = []
    for t in tickets:
        cache[t.source] = t.destination
    for i in range(length):
        if i == 0:
            route.append(cache['NONE'])
        else:
            route.append(cache[route[i-1]])

    return route
