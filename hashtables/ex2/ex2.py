#! /joe/opt/conda/bin/python
#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    des = {}
    # make a ht with the dest as the keys and the values as the source
    tups = []
    for i in tickets:
        tups += [(i.source, i.destination)]
    print(tups)

    return None


if __name__ == '__main__':
    # literally should not change since it's in order
    reconstruct_trip(
        [Ticket(None, 'LAX'),
         Ticket('LAX', 'MIA'),
         Ticket('MIA', None)], 3)

    # now something a bit more complex
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")
    tickets = [
        ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7,
        ticket_8, ticket_9, ticket_10
    ]
    reconstruct_trip(tickets, 10)

    print("main cond.")
