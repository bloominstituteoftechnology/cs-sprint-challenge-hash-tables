#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

d = {}

tickets = [
    Ticket( source= "PIT", destination= "ORD" ),
    Ticket( source= "XNA", destination= "CID" ),
    Ticket( source= "SFO", destination= "BHM" ),
    Ticket( source= "FLG", destination= "XNA" ),
    Ticket( source= "NONE", destination= "LAX"),
    Ticket( source= "LAX", destination= "SFO" ),
    Ticket( source= "CID", destination= "SLC" ),
    Ticket( source= "ORD", destination= "NONE" ),
    Ticket( source= "SLC", destination= "PIT" ),
    Ticket( source= "BHM", destination= "FLG" )
]

def reconstruct_trip(tickets, length):
    #initiate route list
    route = []
    # initiate dictionary of tickets
    for ticket in tickets:
        if ticket not in d:
            d[ticket.source] = ticket.destination


# check a ticket
#if the source of that ticket is none, then append the value to the route
# this makes the first step of the route
    for ticket in d:
        if ticket == "NONE":
            route.append(d[ticket])

    
# now for the length of the route - 1
# check the next ticket
# if the source of the next ticket is the destination of the last ticket
# append the value of the next ticket to the list
# check the next ticket

    for i in range(length-1):
        for ticket in d:
            if ticket == route[i]:
                route.append(d[ticket])
    return route