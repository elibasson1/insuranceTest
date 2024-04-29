import requests


class ticket:
    base_url = "https://sandbox-api-falcon.honeycombinsurance.com/open-for-test/"

    # Function to reset tickets
    def reset(self):
        response = requests.get(f"{self.base_url}/reset")
        return response

    # Function to create a ticket
    def create_ticket(self, data):
        response = requests.post(f"{self.base_url}/ticket", json=data)
        return response

    # Function to get ticket by ID
    def get_ticket_by_id(self, ticket_id):
        response = requests.get(f"{self.base_url}/ticket/{ticket_id}")
        return response

    # Function to decline a ticket by ID
    def decline_ticket(self, ticket_id):
        response = requests.post(f"{self.base_url}/ticket/{ticket_id}/decline")
        return response

    # Function to undecline a ticket by ID
    def undecline_ticket(self, ticket_id):
        response = requests.post(f"{self.base_url}/ticket/{ticket_id}/undecline")
        return response

    # Function to set ticket priority by ID
    def set_ticket_priority_by_id(self, ticket_id, priority):
        data = {
            "priority": priority
        }
        response = requests.post(f"{self.base_url}/ticket/{ticket_id}/priority", json=data)
        return response

    # Function to get all tickets
    def get_all_tickets(self):
        response = requests.get(f"{self.base_url}/tickets")
        return response

    # Function to get open tickets by priority
    def get_open_tickets_by_priority(self):
        response = requests.get(f"{self.base_url}/tickets/statistics")
        return response

    def get_hubspot_card_by_crm_id(self, ticket_id):
        response = requests.get(f"{self.base_url}/hubspot/{ticket_id}")
        return response

    def get_all_hubspot(self):
        response = requests.get(f"{self.base_url}/hubspot")
        return response
