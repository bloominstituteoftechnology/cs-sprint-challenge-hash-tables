#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [None] * length

    dictionary = dict()

    for ticket in tickets:
        dictionary[ticket.source] = ticket.destination
    next = dictionary["NONE"]

    for i in range(0, length):
        route[i] = next
        next = dictionary[next]

    return route
