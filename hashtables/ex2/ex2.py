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
   
    route = [0] * length
    cache = {}
 
    for t in tickets:
        cache[t.source] = t.destination
    
    last = cache['NONE']
    
    for i in range(0, length):
        route[i] = last 
        last = cache[last]

    return route

# ticket_1 = Ticket("PDX", "DCA")
# ticket_2 = Ticket("NONE", "PDX")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# print(reconstruct_trip(tickets, 3))






