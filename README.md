**API Testing and MongoDB Query Task**

**API Overview and Object Types** 

The  service  is  designed  to  manage  tickets  through  various  operations,  including  the creation  of  tickets,  modification  of  their  statuses,  and  adjustment  of  their  priorities. Importantly, it maintains a synchronized state between our internal tickets collection in the MongoDB database and an external CRM system. Every action performed on a ticket within the database is reflected in the CRM system to ensure consistency and real- time data accuracy across both platforms.

**Endpoints:** 

- **Reset Tickets ( GET /reset )** - Resets the ticket databases to their original states
- **Create Ticket ( POST /ticket )** - Creates a new ticket with provided details in the body. Address, nameInsured, and email are required fields. Only one ticket per email is allowed.
- **Get Ticket by ID ( GET /ticket/:id )**
- **Decline Ticket by ID** **( POST /ticket/:id/decline )** - Changes a ticket's status to “decline”by its ID. The ticket must be open (updating both the database and the CRM system)
- **Undecline Ticket by ID ( POST /ticket/:id/undecline )** - Changes a ticket's status to "open" by its ID. The ticket must be declined. (updating both the database and the CRM system)
- **Set Ticket Priority by ID ( POST /ticket/:id/priority ) -** body {“priority”: ?} (updating both the database and the CRM system)
- **Get All Tickets ( GET /tickets )**
- **Get Open Tickets by Priority ( GET /tickets/statistics )**
- **Get Hubspot Card by CRM ID ( GET /hubspot/:crmId )**
- **Get All Hubspot Cards ( GET /hubspot )**

**Object Types:** 

- **Ticket:** 
  - **id**: Number (unique) 
  - crmId: Number 
  - status: String ("open", "decline") 
  - address: String 
  - nameInsured: String 
  - email: String (unique per ticket) 
  - comment: String 
  - priority: String ("Low", "Medium", “High”) 

- **HubSpot Ticket:** 
  - **crmId**: Number (unique) 
  - status: String 
  - address: String 
  - nameInsured: String 
  - email: String 
  - comment: String 
  - priority: String

**Valida on Rules** 

- For creating a ticket, address, nameInsured, and email are required fields.
- Priority set must be one of "Low", "Medium", “High".
- Each email can be associated with only one ticket.
- Decline and undecline operations require the ticket to be in the correct initial state ("open" for declining and "declined" for undeclining).

**Candidate Task** 

**API Tes ng with Postman:** 

1. Write tests to validate the functionality of the endpoints listed above, focusing on creating a ticket, setting priorities, declining/undeclining tickets, fetching all tickets, and getting open tickets by priority.
1. Scenarios to Test include creating a ticket, verifying successful priority assignment, declining and undeclining tickets with correct error handling, and using  /tickets/ statistics  to verify the total number of open tickets for each priority level. 
1. For decline and undecline operations, verify that the database was updated accordingly. Ensure that if a 200 status code is received, the value of the status in the database reflects the action performed.

**Integra on tests (JS)** 

1. write a MongoDB aggregation query to calculate the total number of open tickets for each priority level. This query will be used to validate the output of the /tickets/ statistics endpoint, ensuring that the API and database data are consistent.
1. Test decline/undecline operations and verify they are consistent by using Mongo query

**Notes for the Candidate:** 

- Document all Postman requests and MongoDB queries used for testing and verification.
- Clearly outline any assumptions made during testing.
- Highlight any discrepancies found between the API responses and the database state, including potential reasons and recommendations for addressing these discrepancies.
