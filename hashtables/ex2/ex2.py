#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    cache = {}
    route = [None] * length
    for ticket in tickets:
        start = ticket.source
        destination = ticket.destination
        cache[start] = destination
        if ticket.source == "NONE":
            route[0] = ticket.destination
    for i in range(len(route)-1):
        new_source = route[i]
        new_dest = cache[new_source]
        route[i+1] = new_dest

    return route

