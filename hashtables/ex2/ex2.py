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

    return route

# We can hash each ticket such that the starting location is 
# the key and the destination is the value. Then, when constructing 
# the entire route, the ith location in the route can be found 
# by checking the hash table for the i-1th location.

# create hashtable
# for i in range(3):
    # 
    
    # if not in dict:
        # d[source] = destination

d = {
    'None': 'PDX',
    'PDX': 'DCA',
    'DCA': 'None'
}

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
