import unittest

from ex2 import Ticket, reconstruct_trip
class TestEx2(unittest.TestCase):

    # def test_short_case(self):
    #     ticket_1 = Ticket("NONE", "PDX")
    #     ticket_2 = Ticket("PDX", "DCA")
    #     ticket_3 = Ticket("DCA", "NONE")

    #     tickets_short = [ticket_1, ticket_2, ticket_3]

    #     expected = ["PDX", "DCA", "NONE"]
    #     result_of_short = reconstruct_trip(tickets_short, 3)
    #     print(expected)
    #     print(" -- - - - -")
    #     print(result_of_short)
    #     print(" -- - - - -")
    #     self.assertTrue(expected == result_of_short)
        

    def test_long_case(self):
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

        tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                   ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

        expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
         "SLC", "PIT", "ORD", "NONE"]
        result = reconstruct_trip(tickets, 10)
        print(result)
        print(expected)
        self.assertTrue(expected == result)


if __name__ == '__main__':
    unittest.main()
