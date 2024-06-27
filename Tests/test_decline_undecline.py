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

    def test_decline_un_decline(self):

        # Test from open to un_decline
        response = self.undeclineTicket(Test_ticket.ticketId)
        assert response.status_code == 500
        assert response.json()["message"] == f"ticket w/ ID {Test_ticket.ticketId} must be declined"

        # Test from open to decline.
        response = self.declineTicket(Test_ticket.ticketId)
        assert response.status_code == 200
        assert response.json()["status"] == "decline"
        # Ensure ticket status is now decline
        assert self.getTicketById(Test_ticket.ticketId).json()["status"] == "decline"

        # Test from decline to decline.
        response = self.declineTicket(Test_ticket.ticketId)
        assert response.status_code == 500
        assert response.json()["message"] == f"ticket w/ ID {Test_ticket.ticketId} must be open"

        # Test from decline to un_decline
        response = self.undeclineTicket(Test_ticket.ticketId)
        assert response.status_code == 200
        assert response.json()["status"] == "open"

        # Ensure ticket status is now open
        assert self.getTicketById(Test_ticket.ticketId).json()["status"] == "open"
