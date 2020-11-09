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

def hash_tickets(tickets, length):
    dict = {}
    
    for i in range(length):
        ticket = tickets[i]
        
        source, destination = ticket.get_source(), ticket.get_destination()
        
        dict[source] = destination
    return dict
    
def reconstruct_trip(tickets, length):
    routes = hash_tickets(tickets, length)
    dict  = [routes["NONE"]] * length
    
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


