#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    lookup = {}
    for i in range(length):
        lookup[tickets[i].source] = tickets[i].destination
    
    route = [lookup['NONE']]
    while route[len(route) - 1] is not 'NONE':
        route.append(lookup[route[len(route)-1]])

    return route
