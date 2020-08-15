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
    dict_trip = {}
    route = []

    if len(tickets) == 0:
        print("No tickets, no route")
        return None


    # put tickets in hashtable
    for ticket in tickets:
        dict_trip[ticket.source] = ticket.destination

    # print(dict_trip)    

    # source = NONE is start of route, init airport 
    airport = dict_trip["NONE"]     
    print(airport)  # "PDX"

    # iterate through
    i = 0
    while i < length:
        route.append(airport)
        i += 1
        airport = dict_trip[airport]
    
    print(route)
    return route






ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]


reconstruct_trip(tickets, len(tickets))

# tickets = []
# reconstruct_trip(tickets, len(tickets))