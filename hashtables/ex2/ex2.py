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
    # create a hash table for your tickets
    itinerary = {}
    # start the list
    route = [None] * length
    # iterate over the length to catch all tickets and store them
    for ea_ticket in tickets:
        itinerary[ea_ticket.source] = ea_ticket.destination

    # The ticket for your first flight has a destination with a `source` of `NONE`
    first_flight = itinerary["NONE"]

    # now add to each stop
    for ea_flight in range(length):
        route[ea_flight] = first_flight
        first_flight = itinerary[first_flight]

    return route
