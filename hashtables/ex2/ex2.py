#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    cache = {}
    route = [None]*length

    # populate dictionary
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # find our origin where key is NONE.
    destination = cache['NONE']

    # for each "leg" in expected trip length
    for leg in range(length):
        # store our destinatin in route
        route[leg] = destination
        # next destination is at the key of our current one.
        destination = cache[destination]

    return route
