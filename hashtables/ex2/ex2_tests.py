import unittest

from ex2 import Ticket, reconstruct_trip


class TestEx2(unittest.TestCase):

    def test_short_case(self):
        ticket_1 = Ticket("NONE", "PDX")
        ticket_2 = Ticket("PDX", "DCA")
        ticket_3 = Ticket("DCA", "NONE")

        tickets = [ticket_1, ticket_2, ticket_3]

        expected = ["PDX", "DCA", "NONE"]
        result = reconstruct_trip(tickets, 3)

        self.assertTrue(expected == result)

    def test_long_case(self):

        expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
                    "SLC", "PIT", "ORD", "NONE"]
        result = reconstruct_trip(tickets, 10)

        self.assertTrue(expected == result)


if __name__ == '__main__':
    unittest.main()
