from Data.data import *
from API.api import *


class Test_ticket(ticket):
    ticketId = None

    # Test case for creating a valid ticket
    def test_create_ticket_valid_ticket(self):
        # Create the ticket
        ticketInformation = valid_ticket_info()
        response_create_ticket = self.createTicket(ticketInformation)
        # Check if the ticket was created successfully
        assert response_create_ticket.status_code == 200
        Test_ticket.ticketId = response_create_ticket.json()["id"]

        # Retrieve the ticket by ID
        response_get_ticket = self.getTicketById(Test_ticket.ticketId)
        assert response_get_ticket.status_code == 200

        # Check if the retrieved ticket matches the created ticket data
        assert response_get_ticket.json()["address"] == ticketInformation["address"]
        assert response_get_ticket.json()["nameInsured"] == ticketInformation["nameInsured"]
        assert response_get_ticket.json()["email"] == ticketInformation["email"]
        # Checking if the status of the created ticket is open
        assert response_get_ticket.json()["status"] == "open"

    def test_setting_priorities(self):
        valid_priorities = ["High", "Low", "Medium"]

        # Check priority High Low, Medium
        for priority in valid_priorities:
            set_priority = self.set_ticket_priority_by_id(Test_ticket.ticketId, priority)
            assert set_priority.status_code == 200
            assert set_priority.json()["priority"] == priority

        priority = "wrong"
        set_priority = self.set_ticket_priority_by_id(Test_ticket.ticketId, priority)
        assert set_priority.status_code == 500
        assert set_priority.json()["message"] == (f"Unknown priority provided: {priority}, allowed values:  Low, "
                                                  f"Medium, High")

        priority = ""
        set_priority = self.set_ticket_priority_by_id(Test_ticket.ticketId, priority)
        assert set_priority.status_code == 500
        assert set_priority.json()["message"] == (f"Unknown priority provided: {priority}, allowed values:  Low, "
                                                  f"Medium, High")

        priority = "High"
        id_does_not_exist = -1
        set_priority = self.set_ticket_priority_by_id(id_does_not_exist, priority)
        assert set_priority.status_code == 404
        assert set_priority.json()["message"] == f"no ticket found by ID {id_does_not_exist}"
