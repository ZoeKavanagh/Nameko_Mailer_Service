# Nameko_Mailer_Service

Welcome to Nameko_Mailer_Service, a nameko service that sends an email to a client (landlord) via Mailgun whenever a payment event has been received from a tenant (the payment service when running will dispatch a payment event to the Mailer every 10 seconds).

### Getting Started
In order to run the Mailer Service on your machine, you will need to complete the following steps:

Step 1: Clone this repo

```
git clone XXX
```
Step 2: Install the required packages

```
pip install -r requirements.txt
```
Step 3: Brew install RabbitMQ

```
brew install rabbitmq
```

#### Prerequisites

The Mailer uses [Mailgun](https://mailgun.com) to deliver the emails.  In order for the emails to be sent an email account you can access, you will need to set up your own account with Mailgun and ensure your details, such as 'To: email_address' is updated to the email address you want, the 'api_key' and the 'request_url' which will you be access from Mailgun once you have set up your account and verified your recipient(s) list.

Once you have updated the Mailer with your own email address, Api_key and request_url, you will need to run the service in your terminal through Nameko.

```
nameko run payment_service.payment_service
```
In your terminal, you should see confirmation of emails sent:

![alt text](/images/terminal_demo.png)

To stop running the payment_service, simply cancel it by typing
```
ctrl c
```

You will be able to find the emails dispatched by the service in your chosen inbox:

![alt text](/images/terminal_demo.png))

### Design
After some progression with the development of the program, I decided to move the 'Mailer' and 'Payment_Service' files into their own packages, so that the structure of the code was in line with python application conventions.  This would also mean, if I were to continues with the work on unit/integration tests for each individual package, this would keep testing with Pytest neater, as tests filed would be stored within the package folders.

### Running the tests
The testing framework used for this micro-service, is pytest. To run the existing tests, simply run ``` pytest ``` in the terminal.

### Built With
Nameko - The web framework used
Python3
Pytest - The test framework used
Faker - Used to generate 'fake data' Feeds
Mailgun - API used to dispatch emails

### Further Improvements to be made
Firstly, I would like to have separated out the formatting of the actual email into a separate class and having the actual send_request as an individual function.  This would have made testing easier (mocking the request_url for instance), the code more easy to read and generally cleaner.

Separate out unit tests and integration tests to separate files and create both for the 'payment_service' package also.

I would also have included more 'Raise Errors' to ensure more edge-cases could be caught.
