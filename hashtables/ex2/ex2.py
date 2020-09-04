#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

cache = {}
def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    arr = []
    for i in tickets:
        cache[i.source] = i.destination
        print(i.source)
        if i.source == 'NONE':
            print('= None')
            arr.append(i.destination)
    source = arr[0]
    while len(arr) < length:
        source = cache[source]
        arr.append(source)
        #print(arr)
        
    
        
    #print(cache)
    return arr
    
    # place = None
    # while len(arr) < length:
    #     if 

        #cache{self.source} = self.destination

    #return route
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
print(reconstruct_trip(tickets, len(tickets)))