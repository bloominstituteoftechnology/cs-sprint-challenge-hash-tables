#  Hint:  You may not need all of these.  Remove the unused functions.
from collections import defaultdict
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    trip_dictionary = {}
    route = []
    for tic in tickets:
        trip_dictionary[tic.source] = tic.destination
        
    next_airport = trip_dictionary["NONE"]
    for _ in range(length - 1):
        route.append(next_airport)
        next_airport = trip_dictionary[next_airport]
    route.append("NONE")

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets2 = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets2, len(tickets2))