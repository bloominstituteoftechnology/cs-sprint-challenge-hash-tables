#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    # source represents the starting airport
    # destination represents the next airport
    # first flight has a destination with a source of NONE
    # final flight has a destination of NONE

trip_array = []
trip_dict = {}
def reconstruct_trip(tickets, length):
    for ticket in tickets:
        trip_dict[ticket.source] = ticket.destination
        
    initial_flight = trip_dict["NONE"]
    trip_array.append(initial_flight)
    next_flight = trip_dict[initial_flight]
    while next_flight != "NONE":
        trip_array.append(next_flight)
        next_flight = trip_dict[next_flight]
    
    trip_array.append(next_flight)
    
    route = trip_array
    

    return route
