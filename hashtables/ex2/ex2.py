# Write a function (reconstruct_trip) to reconstruct your trip from your mass of flight tickets
#
# The ticket for your first flight has a destination with a source of NONE, 
# The ticket for your final flight has a source with a destination of NONE.
#
# Your function should output an array of strings with the entire route of your trip. 
# For given example, it should look like this:
# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
# 
# Should run as O(N)

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        """
        self - string represents the starting airport
        destination - string represents the next airport along trip
        """
        self.source = source
        self.destination = destination
        # can be solved with hash table if we treat source as key and destination as value

def reconstruct_trip(tickets, length):
    """
    tickets = list of tickets
    length = length of tickets list
    """
    # hash table to store route's airport source and destination info
    cache = {}
    # initialize route array, next we need to add the original source airport
    route = [None] * length

    # iterate thru each ticket and store its destination in the ht
    for t in tickets:
        cache[t.source] = t.destination

    # first ticket along the route has NONE source, so we start there
    dest = cache["NONE"]

    # next we find each ticket's next destination and add it to the destinations array
    # flight is current ticket
    for flight in range(length):
        # record value of next destination
        route[flight] = dest
        # the next destination is the value in the ht, the key is the destination just added to the array 
        # aka the next flight in the trip
        # continue until complete
        dest = cache[dest]

    return route


# testing
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

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

length = len(tickets)

print(reconstruct_trip(tickets, length))