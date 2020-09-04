#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination



## First ticket would source location of None
# Start here, use it's destination to get next destination, and repeat

def reconstruct_trip(tickets, length):
    ## Dict
    ticket_source = {}

    # iterate through our tickets and find our ticket with Source None
    for ticket in tickets:
    	ticket_source[ticket.source] = ticket 

    	

    return route
