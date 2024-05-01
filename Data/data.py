import secrets


def email_generator():
    return f"{secrets.token_hex(2)}@gmail.com"


def valid_ticket_info():
    email = email_generator()

    ticket_data = {
        "address": "Haifa",
        "nameInsured": "TEST 1",
        "email": email
    }
    return ticket_data


def ticket_missing_address():
    email = email_generator()

    ticket_data = {
        "nameInsured": "TEST 2",
        "email": email
    }
    return ticket_data


def ticket_missing_email():
    ticket_data = {
        "address": "Haifa",
        "nameInsured": "TEST 1",
    }
    return ticket_data


def ticket_missing_name_insured():
    email = email_generator()

    ticket_data = {
        "address": "Haifa",
        "email": email
    }
    return ticket_data


def duplicate_mail(email):
    ticket_data = {
        "address": "Haifa",
        "nameInsured": "TEST 1",
        "email": email
    }
    return ticket_data
