from Data.data import *
from API.api import *


class Test_ticket(ticket):
    ticket_id = None

    # Test case for creating a valid ticket
    def test_create_ticket_valid_ticket(self):
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

    def test_decline_un_decline(self):

        # Test from open to un_decline
        response = self.undecline_ticket(Test_ticket.ticket_id)
        assert response.status_code == 500
        assert response.json()["message"] == f"ticket w/ ID {Test_ticket.ticket_id} must be declined"

        # Test from open to decline.
        response = self.decline_ticket(Test_ticket.ticket_id)
        assert response.status_code == 200
        assert response.json()["status"] == "decline"
        # Ensure ticket status is now decline
        assert self.get_ticket_by_id(Test_ticket.ticket_id).json()["status"] == "decline"

        # Test from decline to decline.
        response = self.decline_ticket(Test_ticket.ticket_id)
        assert response.status_code == 500
        assert response.json()["message"] == f"ticket w/ ID {Test_ticket.ticket_id} must be open"

        # Test from decline to un_decline
        response = self.undecline_ticket(Test_ticket.ticket_id)
        assert response.status_code == 200
        assert response.json()["status"] == "open"

        # Ensure ticket status is now open
        assert self.get_ticket_by_id(Test_ticket.ticket_id).json()["status"] == "open"
