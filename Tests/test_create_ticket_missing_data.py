from Data.data import *
from API.api import *


class Test_ticket(ticket):

    def test_create_ticket_missing_address(self):
        ticketInformation = ticket_missing_address()
        response_create_ticket = self.createTicket(ticketInformation)

        assert response_create_ticket.status_code == 400
        assert response_create_ticket.json()["message"] == "address, nameInsured and email are required"

    def test_create_ticket_missing_email(self):
        ticketInformation = ticket_missing_email()
        response_create_ticket = self.createTicket(ticketInformation)

        assert response_create_ticket.status_code == 400
        assert response_create_ticket.json()["message"] == "address, nameInsured and email are required"

    def test_create_ticket_missing_name_insured(self):
        ticketInformation = ticket_missing_name_insured()
        response_create_ticket = self.createTicket(ticketInformation)

        assert response_create_ticket.status_code == 400
        assert response_create_ticket.json()["message"] == "address, nameInsured and email are required"
