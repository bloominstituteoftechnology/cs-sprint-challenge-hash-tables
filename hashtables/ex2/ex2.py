#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # set up cache
    cache = {}
    # setting up list (route)
    route = [None] * length

    # go through all tickets
    for ticket in tickets:
        # set cache source
        cache[ticket.source] = ticket.destination
    # reset my cache
    next = cache["NONE"]

    for r in range(0, length):  # iterate through range
        # set route cache
        route[r] = next
        # set the next destination to cache
        next = cache[next]

    return route
