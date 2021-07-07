#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        


def reconstruct_trip(tickets, length):
    route = [None] * length
    cache = {}
    for t in tickets: 
        cache[t.source] = t.destination
    dest = cache["None"]

    for flight in range(0, length): 
        route[flight] = dest
    dest = cache[dest]
    return route




# Test cases
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]

# MVP done