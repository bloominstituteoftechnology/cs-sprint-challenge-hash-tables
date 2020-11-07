#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hash_table = {}
    route = []

    for ticket in tickets:
        hash_table[ticket.source] = ticket.destination
        if ticket.source == "NONE": # add first flight
            route.append(ticket.destination)
            
    destination = route[0]
    while destination != "NONE":
        destination = hash_table[destination]
        route.append(destination)
        
    return route
