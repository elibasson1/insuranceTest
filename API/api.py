import requests


class ticket:
    baseUrl = "https://sandbox-api-falcon.honeycombinsurance.com/open-for-test/"

    # Function to reset tickets
    def reset(self):
        response = requests.get(f"{self.baseUrl}/reset")
        return response

    # Function to create a ticket
    def createTicket(self, data):
        response = requests.post(f"{self.baseUrl}/ticket", json=data)
        return response

    # Function to get ticket by ID
    def getTicketById(self, ticketId):
        response = requests.get(f"{self.baseUrl}/ticket/{ticketId}")
        return response

    # Function to decline a ticket by ID
    def declineTicket(self, ticketId):
        response = requests.post(f"{self.baseUrl}/ticket/{ticketId}/decline")
        return response

    # Function to underline a ticket by ID
    def undeclineTicket(self, ticketId):
        response = requests.post(f"{self.baseUrl}/ticket/{ticketId}/undecline")
        return response

    # Function to set ticket priority by ID
    def set_ticket_priority_by_id(self, ticketId, priority):
        data = {
            "priority": priority
        }
        response = requests.post(f"{self.baseUrl}/ticket/{ticketId}/priority", json=data)
        return response

    # Function to get all tickets
    def get_all_tickets(self):
        response = requests.get(f"{self.baseUrl}/tickets")
        return response

    # Function to get open tickets by priority
    def get_open_tickets_by_priority(self):
        response = requests.get(f"{self.baseUrl}/tickets/statistics")
        return response

    def get_hubspot_card_by_crm_id(self, ticketId):
        response = requests.get(f"{self.baseUrl}/hubspot/{ticketId}")
        return response

    def get_all_hubspot(self):
        response = requests.get(f"{self.baseUrl}/hubspot")
        return response
