#  Hint:  You may not need all of these.  Remove the unused functions.

# First Ticket: Source = None / Destination = next_airport
# Last Ticket: Source = prev_airport / Destination = None

# Output = Array of strings representing the entire route of the trip

# Input will always be a valid ticket so no check is necessary

# Hash each ticket so that the source is the ley and destination is
# the value then building the route would mean the ith location can
# be found by checking cache for i - 1.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    # Initialize a list for the length of the tickets list
    route = [None] * length

    # Loop over each ticket in the list and add source as the key
    # and destination as the value to the cache
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # The first ticket should have a source equal to NONE
    destination = cache["NONE"]

    # For each ticket in the list set the destination to the route list
    # then set the source of the next trip to the previous trips destination
    for trip in range(length):
        route[trip] = destination
        print(route)

        destination = cache[destination]

    return route


# TEST TEST TEST
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

length = len(tickets)

print(reconstruct_trip(tickets, length))
