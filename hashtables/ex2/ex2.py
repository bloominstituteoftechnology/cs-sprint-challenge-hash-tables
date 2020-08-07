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
    # We want to return a list of all our destinations in order
    # Our starting ticket will have a source of None and a destination
    # Our ending destination will have a destination of none
    # we want to run this function in linear time
    # our output should be a list of city names

    # create a dictionary that contains the source as the key and the destination as the value
    cities = {city.source: city.destination for city in tickets}
    # create a list to hold the city names
    itinerary = []
    current = cities["NONE"]
    # create a loop that checks to see if the value of destination is none
    for i in range(length):
        itinerary.append(current)
        current = cities[current]

    return itinerary
    

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
print(result)