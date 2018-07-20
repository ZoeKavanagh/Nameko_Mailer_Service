from mailer.mailer import Mailer
from mailer.mailer import ApiKeyError
from payment_service.payment_service import PaymentService

import pytest
from mock import call, patch, Mock

from nameko.events import event_handler
from nameko.testing.utils import get_extension
from nameko.standalone.events import event_dispatcher
from nameko.testing.services import entrypoint_waiter

import requests
import requests_mock

import config

mailer = Mailer()

@pytest.fixture
def mock_event():
    payload = {
        'client': {
            'name': 'zoe',
            'email': 'zoe@zoe.com'
        },
        'payee': {
            'name': 'Phil',
            'email': 'phil@phil.com'
        },
        'payment': {
            'amount': 10000,
            'currency': "GBP"
        }
    }
    return ("payment_received", payload)

def test_init_mailer_success():
    assert mailer.api_key == config.api_key

def test_init_mailer_failure():
    config.api_key = None
    with pytest.raises(ApiKeyError):
        Mailer()

def test_send_mail():
    mailer.send_mail = Mock()
    mailer.send_mail(mock_event())

    mailer.send_mail.assert_called_with(mock_event())

class TestMailer:

    name = "test_mailer"

    @event_handler("test_mailer", "event_type")
    def handle_event(self, payload):
        print("test_payment_service", payload)


def test_payment_service(container_factory, rabbit_config):

    container = container_factory(TestMailer, rabbit_config)
    container.start()

    dispatch = event_dispatcher(rabbit_config)

    # prints "service b received payload" before "exited"
    with entrypoint_waiter(container, 'handle_event'):
        dispatch("test_mailer", "event_type", "payload")
    print("exited")
