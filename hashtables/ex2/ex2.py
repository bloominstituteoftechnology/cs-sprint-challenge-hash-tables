#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length
    cache = {}

    for v in tickets:
        cache[v.source] = v.destination
    next = cache["NONE"]

    for current in range(length):
        route[current] = next
        next = cache[next]
    return route
