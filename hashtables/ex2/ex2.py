#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    table = {}
    route = []
    for ticket in tickets:
        if ticket.source == "NONE":
            table['start'] = ticket.destination
        else:
            table[ticket.source] = ticket.destination
    
    key = 'start'
    while table[key] != 'NONE':
        route.append(table[key])
        key = table[key]
        

    return route
