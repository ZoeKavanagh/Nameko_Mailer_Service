from nameko.events import event_handler
import requests
import config

class ApiKeyError(Exception):
    pass

class EmailAddressError(Exception):
    pass

class Mailer(object):
    name = "mailer"

    def __init__(self):
        self.email_address = config.email_address
        self.request_url = config.request_url
        self.api_key = config.api_key

        if self.api_key is None:
            raise ApiKeyError

        if self.email_address is None:
            raise EmailAddressError

    @event_handler("payments", "payment_received")

    def send_mail(self, payload):
        amount = payload['payment']['amount']
        format_amount = '{:,}'.format(amount)

        response = requests.post(
            self.request_url,
            auth=("api", self.api_key),
            data={"from": "Payment Service payments@student.com",
                  "to": [self.email_address],
                  "subject": "Payment Confirmation - Student.com",
                  "text": f"Dear {payload['payee']['name']},\n\nYou have received a payment of {format_amount} {payload['payment']['currency']} from {payload['client']['name']} ({payload['client']['email']}).\n\n Yours,\nstudent.com"})

        print(response.text)
        print(response.status_code)

        return response
