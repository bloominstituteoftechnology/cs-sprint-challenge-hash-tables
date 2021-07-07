#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    route = [None] * length
    
    travel_dict = {}
    
    for ticket in tickets:
        travel_dict[ticket.source] = ticket.destination
    next = travel_dict["NONE"]
        
    for c in range(0, length):
        route[c] = next
        next = travel_dict[next]
    
    return route
