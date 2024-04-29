from Data.data import *
from API.api import *


class Test_ticket(ticket):
    ticket_id = None

    # Test case for creating a valid ticket
    def test_create_valid_ticket(self):
        # Create the ticket
        ticket_information = valid_ticket_info()
        response_create_ticket = self.create_ticket(ticket_information)
        # Check if the ticket was created successfully
        assert response_create_ticket.status_code == 200
        Test_ticket.ticket_id = response_create_ticket.json()["id"]

        # Retrieve the ticket by ID
        response_get_ticket = self.get_ticket_by_id(Test_ticket.ticket_id)
        assert response_get_ticket.status_code == 200

        # Check if the retrieved ticket matches the created ticket data
        assert response_get_ticket.json()["address"] == ticket_information["address"]
        assert response_get_ticket.json()["nameInsured"] == ticket_information["nameInsured"]
        assert response_get_ticket.json()["email"] == ticket_information["email"]
        # Checking if the status of the created ticket is open
        assert response_get_ticket.json()["status"] == "open"
