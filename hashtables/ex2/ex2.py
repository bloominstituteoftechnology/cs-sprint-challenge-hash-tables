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
    route = []
    table = {}
    for ticket in tickets:
        table[ticket.source] = ticket.destination

    route.append(table['NONE'])

    for i in range(1, length):
        next_source = route[i-1]
        if next_source in table:
            route.append(table[next_source])

    return route
