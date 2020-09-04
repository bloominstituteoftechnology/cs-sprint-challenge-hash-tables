#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    src_tic = {x.source:x for x in tickets}

    route = []

    curr_ticket = src_tic["NONE"]
    while curr_ticket.destination != "NONE":
        route.append(curr_ticket.destination)
        curr_ticket = src_tic[curr_ticket.destination]

    route.append(curr_ticket.destination)
    return route
