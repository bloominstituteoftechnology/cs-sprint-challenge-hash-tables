#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    # all tickets
    cache = {}

    # add all tickets to cache
    for t in tickets:
        cache[t.source] = t.destination

    # list that returns destination
    itinerary = []

    # which stop we're currently on
    current = 'NONE'

    for i in range(length):

        # append the value to the trip list
        itinerary.append(cache[current])

        # set a new current
        current = cache[current]

    return itinerary

# We can hash each ticket such that the starting location is 
# the key and the destination is the value. Then, when constructing 
# the entire route, the ith location in the route can be found 
# by checking the hash table for the i-1th location.





d = {
    'None': 'PDX',
    'PDX': 'DCA',
    'DCA': 'None'
}

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
print(result)
