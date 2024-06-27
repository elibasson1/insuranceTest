from Data.data import *
from API.api import *


class Test_ticket(ticket):
    ticketId = None

    # Test case for creating a valid ticket
    def test_create_valid_ticket(self):
        # Create the ticket
        ticketInformation = valid_ticket_info()
        response_create_ticket = self.createTicket(ticketInformation)
        # Check if the ticket was created successfully
        assert response_create_ticket.status_code == 200
        Test_ticket.ticketId = response_create_ticket.json()["id"]

        # Retrieve the ticket by ID
        response_get_ticket = self.getTicketById(Test_ticket.ticketId)
        assert response_get_ticket.status_code == 200

        retrieve_ticket = response_get_ticket.json()
        # Check if the retrieved ticket matches the created ticket data
        assert retrieve_ticket["address"] == ticketInformation["address"]
        assert retrieve_ticket["nameInsured"] == ticketInformation["nameInsured"]
        assert retrieve_ticket["email"] == ticketInformation["email"]
        assert retrieve_ticket["status"] == "open"

        email = retrieve_ticket["email"]
        ticketInformation = duplicate_mail(email)

        # Check duplicate mail
        response_create_ticket = self.createTicket(ticketInformation)
        assert response_create_ticket.status_code == 400
        assert response_create_ticket.json()["message"] == "ticket for this email already exists"
