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

    q = dict()
    for ticket in tickets:
        q[ticket.source] = ticket.destination
    next = q["NONE"]

    for curr in range(0, length):
        route[curr] = next
        next = q[next]

    return route
