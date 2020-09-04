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

    	source_none_ticket = ticket_source["NONE"] # Gotcha

    	# now let's set our route up

    	my_route = []

    	while True: 
    		route.append(source_none_ticket)

    		#if we see NONE for destination, keep going
    		if source_none_ticket.destination == "NONE":
    			break

    		# set next ticket to the current tickets destination 
    		source_none_ticket = ticket_source[source_none_ticket.destination]

    	return my_route




    return route
