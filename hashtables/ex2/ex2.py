#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    tickets_by_source = {}

    for ticket in tickets:
        tickets_by_source[ticket.source] = ticket

    # first ticket would be source of "NONE"
    # use it's destination to get next

    current_ticket = tickets_by_source["NONE"]
    
    route = []

    while True:
        route.append(current_ticket.destination)
    
        if current_ticket.destination == "NONE":
            break

        current_ticket = tickets_by_source[current_ticket.destination]

    return route
