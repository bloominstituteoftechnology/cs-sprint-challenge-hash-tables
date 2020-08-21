class Ticket:
    """
    A flight ticket.
    """
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Links flight tickets together into a continuous one-way trip.
    """
    # Create empty dictionary of flight routes that we will populate with the 
    # tickets' flights' info, and list "route" for our linked-together overall route:
    flights = {}
    route = []
    # Populate dictionary with all flight tickets, with keys as source airports 
    # and values as destination airports (i.e., like an adjacency list:
    for ticket in tickets:
        source, destination = ticket.source, ticket.destination
        if source not in flights:
            flights[source] = destination  # Note: Assumes only 1 visit per airport, based on the prompt.
    
    # Link together tickets into a continuous route, and return a list with the route:
    # Start with starting flight:
    source_airport = "NONE"
    next_stop = flights[source_airport]
    # Follow the flights to add the rest of the route:
    while next_stop is not "NONE":
        next_stop = flights[source_airport]
        route.append(next_stop)
        # Increment (move forward 1 stop):
        source_airport = next_stop

    return route
