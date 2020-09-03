#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    flights = dict()
    route = [None] * length

    for ticket in tickets:
        flights[ticket.source] = ticket.destination
    
    destination = flights['NONE']

    for num in range(length):
        route[num] = destination
        destination = flights[destination]

    return route