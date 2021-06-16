#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Will first put the items in a cache
    my_cache = {}
    route = []
    lookfor = ""
    for ticket in tickets:        
        # will put source as the key and destination as the value
        # if we find the source that is none we will not put this 
        # in the hash tabel but will put that in the route list (array) to start
        if ticket.source == "NONE":
            route.append(ticket.destination)
            lookfor = ticket.destination
        else:
            my_cache[ticket.source] = ticket.destination
   
    while True:
        if lookfor in my_cache:
            
            # will want to then append 
            # the route with the destination
            lookfor = my_cache[lookfor]
            route.append(lookfor)
            if lookfor == "NONE":
                break
            
                
    
            
        


    return route
