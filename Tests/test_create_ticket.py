from Data.data import *
from API.api import *


class TestTicket(ticket):
    ticketId = None

    # Test case for creating a valid ticket
    def test_create_valid_ticket(self):
        # Create the ticket
        ticketInformation = valid_ticket_info()
        response = self.createTicket(ticketInformation)
        # Check if the ticket was created successfully
        assert response.status_code == 200
        TestTicket.ticketId = response.json()["id"]

        # Retrieve the ticket by ID
        retrieveResponse = self.getTicketById(TestTicket.ticketId)
        assert retrieveResponse.status_code == 200
        retrievedTicket = retrieveResponse.json()

        # Check if the retrieved ticket matches the created ticket data
        assert retrievedTicket["address"] == ticketInformation["address"]
        assert retrievedTicket["nameInsured"] == ticketInformation["nameInsured"]
        assert retrievedTicket["email"] == ticketInformation["email"]
        # Checking if the status of the created ticket is open
        assert retrievedTicket["status"] == "open"
