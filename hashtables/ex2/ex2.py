class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Given a list of tickets that form a valid ticket chain, such that the
    destination of each ticket is the source of the next, output an array of
    strings with the entire route of the trip in order. Input need not be
    ordered.
    """

    # Build a lookup table that gives the next step in the itinerary for any
    # given location.
    lookup = {ticket.source: ticket.destination for ticket in tickets}

    # Initialize a list of strings for the output.
    route = [''] * length

    # Add each location to the output in order, following the source ->
    # destination links defined by the lookup table.
    route[0] = lookup['NONE']
    for i in range(1, length):
        route[i] = lookup[route[i-1]]

    # Return the completed list.
    return route
