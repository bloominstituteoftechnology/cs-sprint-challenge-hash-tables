class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    # `source` = starting airport
    def get_source(self):
        return self.source
    
    # `destination` = next airport along my trip
    def get_destination(self):
        return self.destination

#  Hash each ticket such that the starting location is the key and the destination is the value.
def hash_tickets(tickets, length):
    dict = {}
    # looop through array of tickets
    for i in range(length):
        ticket = tickets[i]
        # add starting airport(source) as key and destination as value
        source, destination = ticket.get_source(), ticket.get_destination()
        # destination equal to source
        dict[source] = destination
    return dict
    
# find the starting airport that equals to NONE and its destination. Then that destination is equal to another ticket starting and so on
# length = the length of the array
def reconstruct_trip(tickets, length):
    routes = hash_tickets(tickets, length)
    dict  = [routes["NONE"]] * length
    
    # the `i`th location in the route can be found by checking the hash table for the `i-1`th location
    for i in range(1, len(dict)):
        dict[i] = routes[dict[i -1]]
    return dict


# Driver code
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "CID")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("CID", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))

# Expected Output = ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD", "NONE"]
