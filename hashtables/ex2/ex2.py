#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    routes = {}
    for ticket in tickets:
      routes[ticket.source] = ticket.destination

    ans = [routes['NONE']]
    for i in range(len(tickets)-2):
      next = routes[ans[i]]
      ans.append(next)
      if i == len(tickets)-3:
        ans.append('NONE')

    return ans
