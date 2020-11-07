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
    # Create a hashtable
    hashtable = {}

    # Initialize a list for the length of the tickets list
    route = [None] * length
    # Loop over each ticket in the list and add source as the key
    # and destination as the value to the cache
    for ticket in tickets:
        hashtable[ticket.source] = ticket.destination
    # The first ticket should have a source equal to NONE
    next_stop = hashtable["NONE"]
    # For each ticket in the list set the destination to the route list
    # then set the source of the next trip to the previous trip's destination
    for trip in range(0, length):
        route[trip] = next_stop
        next_stop = hashtable[next_stop]

    return route



ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, len(tickets)))
