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

        retrieve_ticket = response_get_ticket.json()
        # Check if the retrieved ticket matches the created ticket data
        assert retrieve_ticket["address"] == ticket_information["address"]
        assert retrieve_ticket["nameInsured"] == ticket_information["nameInsured"]
        assert retrieve_ticket["email"] == ticket_information["email"]
        assert retrieve_ticket["status"] == "open"

        email = retrieve_ticket["email"]
        ticket_information = duplicate_mail(email)

        # Check duplicate mail
        response_create_ticket = self.create_ticket(ticket_information)
        assert response_create_ticket.status_code == 400
        assert response_create_ticket.json()["message"] == "ticket for this email already exists"
