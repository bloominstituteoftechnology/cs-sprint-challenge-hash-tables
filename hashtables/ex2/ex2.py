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
    lookup = {ticket.source: ticket.destination for ticket in tickets}
    location = lookup["NONE"] 
    route = [location]

    while location != "NONE":  #if not none then 
        location = lookup[location] #look up location
        route.append(location) #add location
    return route
