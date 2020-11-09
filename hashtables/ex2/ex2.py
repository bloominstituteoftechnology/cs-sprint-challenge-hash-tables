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
    cache = {}
    route = [None] * length

    # loop through indexs in tickets
    for ticket in tickets:

        if ticket.source == "NONE":
            # ticket equals first flight
            route[0] = ticket.destination
        # add ticket source to cache
        cache[ticket.source] = ticket.destination

    for i in range(1, length):
        route[i] = cache[route[i-1]]

    return route
