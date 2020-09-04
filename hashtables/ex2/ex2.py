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
    	# now that we can use the ticket source as the 'ticket' we can find the ticket with source None
    	current_ticket = ticket_source['NONE']
    	# Gotcha
    	# now let's set our route up
    	route = []

    	while True: 
    		route.append(current_ticket.destination)

    		#if we see NONE for destination, keep going
    		if current_ticket.destination == "NONE":
    			break

    		# set next ticket to the current tickets destination 
    		current_ticket = ticket_source[current_ticket.destination]

    	return route
