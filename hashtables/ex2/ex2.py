#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    flight_dict = {}
    route= []
    for t in tickets:
        flight_dict[t.source] = t.destination
      
    source_flight = 'NONE'
    for i in range(length):
        print('before', source_flight)
        source_flight = flight_dict.get(source_flight)
        print('after', source_flight)
        route.append(source_flight) 
    print('source', source_flight)
        
    # route.append(t.destination)
    print(route)
    # Your code here
    # start where the source is None
   
    # last flight has destination of None

    return route




