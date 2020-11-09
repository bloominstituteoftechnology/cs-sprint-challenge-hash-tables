#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = [None] * length
    ticket_dict = {}

    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    next_ticket = ticket_dict["NONE"]

    for i in range(length):
        route[i] = next_ticket
        next_ticket = ticket_dict[next_ticket]

    return route