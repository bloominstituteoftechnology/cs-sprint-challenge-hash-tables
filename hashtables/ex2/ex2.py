#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f'\n(source: {self.source}, destination: {self.destination})\n'

def reconstruct_trip(tickets, length):
    # Initialize storage hash table
    dictionary = {}
    route = []

    # Map tickets into hash table
    for ticket in tickets:
        dictionary[ticket.source] = ticket.destination
        
    # Set pointer to first flight and loop
    next_flight = dictionary['NONE']
    while next_flight != "NONE":
        # add flight to route array
        route.append(next_flight)
        # update pointer to next destination
        next_flight = dictionary[next_flight] 
    
    # Reached the final destination, add None 
    route.append("NONE")

    # Return the 
    return route


tickets = [
    Ticket("PIT", "ORD" ),
    Ticket("XNA", "CID" ),
    Ticket("SFO", "BHM" ),
    Ticket("FLG", "XNA" ),
    Ticket("NONE", "LAX" ),
    Ticket("LAX", "SFO" ),
    Ticket("CID", "SLC" ),
    Ticket("ORD", "NONE" ),
    Ticket("SLC", "PIT" ),
    Ticket("BHM", "FLG" )
]

print(reconstruct_trip(tickets, 10))