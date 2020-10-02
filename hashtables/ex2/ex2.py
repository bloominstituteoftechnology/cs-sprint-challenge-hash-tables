#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Your code here
    
    tickets_dict = {} # create a dict for each gateway
    
    # for each leg in a ticket, if it's not in the dict, pair source & destination gateways
    for i in tickets:
        if i not in tickets_dict:
            tickets_dict[i.source] = i.destination
    
    gateway = tickets_dict["NONE"] # starting gateway always NONE
    route = [gateway] # route starts with starting point NONE and then add each gateway stop

    # append each leg to each other with the source of one being the destination of previous one
    for i in range(length-1):
        route.append(tickets_dict[route[i]])

    # print(route)
    return route