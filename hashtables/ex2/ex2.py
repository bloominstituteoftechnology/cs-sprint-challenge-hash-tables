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
    route = {}
    arr = []
    print()
    
    for t in tickets:
        print (t.source, t.destination)
        if t.source  not in route:
            route[t.source] = t.destination
        if t.source == "NONE":
            arr.append(t.destination)
            
    for i in range(length -1) :
        arr.append(route[arr[i]])     
    return arr


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]

print (reconstruct_trip(tickets, 3))
