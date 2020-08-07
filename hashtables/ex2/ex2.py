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
    location = {}

    for ticket in tickets:
        location[ticket.source] = ticket.destination
    next = location["NONE"]

    for i in range(0, length):
        route[i] = next
        next = location[next]

    return route
