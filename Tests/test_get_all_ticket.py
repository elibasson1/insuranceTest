import json

from Data.data import *
from API.api import *


class Test_ticket(ticket):

    def test_get_all_ticket(self):
        response_get_tickets = self.get_all_tickets()
        assert response_get_tickets.status_code == 200

        # Pretty printed data
        json_data = response_get_tickets.text
        obj = json.loads(json_data)
        json_formatted_str = json.dumps(obj, indent=2)
        print(json_formatted_str)
