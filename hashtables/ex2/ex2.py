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
    ht = {}
    length = len(tickets)
    for ticket in tickets:
        # if ticket.source != "NONE":
        ht[ticket.source] = ticket.destination
    route = []
    
    key = "NONE"
    route.append(ht[key])
    while ht[key] != 'NONE':
        key = ht[key]
        route.append(ht[key])

    # print('route', route)
    return route
