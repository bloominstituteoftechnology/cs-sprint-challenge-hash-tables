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
    storage = dict()    

    for ticket in tickets:
        storage[ticket.source] = ticket.destination        

    next_destination = storage['NONE']

    for i in range(length):
        route[i] = next_destination
        next_destination = storage[next_destination]

    return route