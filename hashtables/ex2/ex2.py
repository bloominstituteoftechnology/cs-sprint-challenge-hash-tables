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
    
    #loop thru tickets and cache destination as source
    for t in tickets:
        cache[t.source] = t.destination
   
    # departure set to 'NONE's destination
    dep = cache['NONE']
    
    # loop through flights, setting destination from source
    for i in range(0, length):
        route[i] = dep 
        dep = cache[dep]

    return route

# ticket_1 = Ticket("PDX", "DCA")
# ticket_2 = Ticket("NONE", "PDX")
# ticket_3 = Ticket("DCA", "BEN")
# ticket_4 = Ticket("BEN", "WAS")
# ticket_5 = Ticket("WAS", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5]

# print(reconstruct_trip(tickets, 5))






