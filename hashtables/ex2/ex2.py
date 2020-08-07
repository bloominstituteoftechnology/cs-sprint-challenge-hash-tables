#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    tickets_source = {}
    
    for ticket in tickets:
        tickets_source[ticket.source] = ticket

    # first ticket would be source of "NONE"

    current_ticket = tickets_source["NONE"]
    
    route = []
    # use it's destination to get next
    while True:
        route.append(current_ticket.destination)
    
        if current_ticket.destination == "NONE":
            break

        current_ticket = tickets_source[current_ticket.destination]

    return route
