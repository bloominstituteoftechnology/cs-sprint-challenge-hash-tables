
class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination


def reconstruct_trip(tickets, length):
	cache = {}
	route = [None] * length

	for ticket in tickets:
		cache[ticket.source] = ticket.destination

	destination = cache["NONE"] # set first destination
	for x in range(length):
		route[x] = destination
		destination = cache[destination]

	return route

