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
    dict = {}

    for ticket in tickets:
        dict[ticket.source] = ticket.destination

    # start with the destination value of the first one, which should have source None
    route = [dict["NONE"]]
    print(f'{route}')
    for i in range(length - 1):
        # start with None
        # Then pass None into the hash table, see what its destination is
        # add the destination
        # then hash the destination and see what the value is (next destination)
        # append that value
        # etc
        route.append(dict[route[i]])
        print(f'{route}')
    

    # print(f'{dict}')

    return route


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
