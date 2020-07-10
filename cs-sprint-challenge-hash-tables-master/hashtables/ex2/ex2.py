#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source # The starting point for a flight
        self.destination = destination # The ending point for a flight


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    # Build up our cache
    for ticket in tickets:
        if ticket.source is None:
            cache['NONE'] = ticket.destination
        if ticket.destination is None:
            cache[ticket.source] = 'NONE'

        cache[ticket.source] = ticket.destination

    # Build up our list of tickets
    ticket_list = []
    connection = True # A starting point connects to a destination
    source = 'NONE'

    while connection is True:
        destination = cache[source]
        source = destination
        ticket_list.append(destination)
        if destination == 'NONE':
            connection = False

    return ticket_list

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "CID")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("CID", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")


tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

reconstruct_trip(tickets, 10)