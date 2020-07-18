#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination


def reconstruct_trip(tickets, length):
	"""
	YOUR CODE HERE
	# Set all of the tickets into our cache
	# Start our route where source equals NONE
	# Reconstruct our route
	"""
	# Your code here
	cache = {}
	for ticket in tickets:
		cache[ticket.source] = ticket.destination

	route = []
	next_tic = cache["NONE"]
	route.append(next_tic)
	while next_tic != "NONE":
	   next_tic = cache[next_tic]
	   route.append(next_tic)

	return route
