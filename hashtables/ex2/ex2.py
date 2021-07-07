# #  Hint:  You may not need all of these.  Remove the unused functions.
# class Ticket:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination

#     def get_source(self):
#         return self.source
    
#     # `destination` = next airport along my trip
#     def get_destination(self):
#         return self.destination


# def reconstruct_trip(tickets, length):
#     """
#     YOUR CODE HERE
#     """
#     # Your code here
#     route = []
#     # loop through array of tickets
#     for i in range(length):
#         ticket = tickets[i]
#         if ticket.get_source != "NONE":
#             ticket.get_destination
#         else:
#             # add starting airport(source) as key and destination as value
#             source, destination = ticket.get_source(), ticket.get_destination()
#             # destination equal to source
#             route[source] = destination

#     return route



    # return route

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    def get_source(self):
        return self.source
    
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
    
    # the `i`th location in the route can be found by checking the hash table for the `i-1`th location
    for i in range(1, len(dict)):
        dict[i] = routes[dict[i -1]]
    return dict