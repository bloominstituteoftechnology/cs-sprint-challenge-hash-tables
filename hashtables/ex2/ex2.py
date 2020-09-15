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

    ticket_source = {}

    for ticket in tickets:
        ticket_source[ticket.source] = ticket

    current_ticket = ticket_source["NONE"]

    route = []

    while True:
        route.append(current_ticket.destination)

        if current_ticket.destination == "NONE":
            break

        current_ticket = ticket_source[current_ticket.destination]

    return route
