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
    # Assume all ticket chains work!
    ticket_cache = {}
    route = [None] * length

    for ticket in tickets:
        ticket_cache[ticket.source] = ticket.destination

    route[0] = ticket_cache["NONE"] #Establishing first ticket

    for i in range(1, length):
        route[i] = ticket_cache[route[i-1]]
    
    print(ticket_cache)


    return route
