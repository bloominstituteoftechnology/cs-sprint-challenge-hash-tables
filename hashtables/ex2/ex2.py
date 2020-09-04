#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length
    cache = {}



    # print(cache)
    for i in range(length):
        # print(cache["PIT"])
        if tickets[i].source == "NONE":
            # sets the first index in route as the value (destination) of the ticket based off the key (source)
            # and in this case we will always want the first index to be the ticket that has NONE as the source.
            route[0] = tickets[i].destination
        # puts tickets into cache dictionary
        cache[tickets[i].source] = tickets[i].destination

    for j in range(length):
        if route[j - 1]:
            route[j] = cache[route[j - 1]]
        # print(route)

    return route

# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
# reconstruct_trip(tickets, 10)