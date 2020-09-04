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
    dict = {}
    for ticket in tickets:
        dict[ticket.source] = ticket.destination

    route = [dict['NONE']]
    find = dict[route[-1]]

    while len(route) < length:
        route.append(find)
        find = dict[find]

    return route