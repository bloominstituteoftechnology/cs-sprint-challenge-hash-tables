#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticket_dict = {}
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    loc = ticket_dict['NONE']
    route = []
    route.append(loc)
    while loc != 'NONE':
        loc = ticket_dict[loc]
        route.append(loc)


    return route
