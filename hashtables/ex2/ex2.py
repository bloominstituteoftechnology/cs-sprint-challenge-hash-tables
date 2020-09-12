#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    given a list of tickets and the number of tickets, finds
    the round-trip through through those tickets.
    """
    
    d = {}
    for ticket in tickets:
        d[ticket.source] = ticket.destination

    ii = "NONE"
    route = []
    for jj in range(length):
        route.append(d[ii])
        ii = d[ii]

    return route
