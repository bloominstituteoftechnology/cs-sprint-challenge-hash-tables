#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


    def get_source(self):
        return self.source
    
    # `destination` = next airport along my trip
    def get_destination(self):
        return self.destination

#  Hash each ticket such that the starting location is the key and the destination is the value.
def hash_tickets(tickets, length):
    dict = {}
    # looop through array of tickets
    for i in range(length):
        ticket = tickets[i]
        # add starting airport(source) as key and destination as value
        source, destination = ticket.get_source(), ticket.get_destination()
        # destination equal to source
        dict[source] = destination
    return dict


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    return route
