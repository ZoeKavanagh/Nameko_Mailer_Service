# Nameko_Mailer_Service

Welcome to Nameko_Mailer_Service, a nameko micro-service that will send an email to a client (landlord) via [Mailgun](https://mailgun.com) whenever a payment 'event' has been received from a tenant (the payment_service, when running, will dispatch a payment event to the Mailer every 10 seconds).

### Getting Started
In order to run the Mailer Service locally, you will need to complete the following steps:

Step 1: Clone this repo

```
git clone https://github.com/ZoeKavanagh/nameko_mailer_service.git
```
Step 2: Install the required packages

```
pip install -r requirements.txt
```
Step 3: Brew install RabbitMQ

```
brew install rabbitmq
```

### Prerequisites

The Mailer uses [Mailgun](https://mailgun.com) to deliver the emails.  In order for the emails to be sent to an email account you can access, you will need to create your own account with Mailgun first.  Once you have done this, you will need to update the Mailer code to ensure your personal details, these include: 1) 'To: email_address' will need updating to an email address you wish to receive the emails to 2) Your own 'api_key' which you will access from Mailgun when you have setup your account 3) The 'request_url', which you will also be able access from Mailgun once you have set up your account.  All personal/'secret' information such as the API_KEY, 'request_url' and 'email_address' can be hidden by adding these details to a config.py file, which will not be updated Github, the actual code within the 'Mailer' will not require updating.  Your config.py file should look something this:


You will need to verify your recipient(s) list to ensure the emails will be received by the chosen address. 

Once you have updated the Mailer || config.py with your own email address, Api_key and request_url, you will need to run the service in your terminal through Nameko.

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

![alt text](/images/email_demo.png), 

### Design
After some progression with the development of the program, I moved the 'Mailer' and 'Payment_Service' files into their own packages, so that the structure of the code was in line with good integration practices and the conventions for Python test discovery.

### Running the tests
The testing framework used for this micro-service, is Pytest. To run the existing tests, simply run ``` pytest ``` in the terminal.

### Built With
 - Nameko - The web framework used
 - Python3
 - Pytest - The test framework used
 - Faker - Used to generate 'fake data' Feeds
 - Mailgun - API used to dispatch emails

### Further Improvements to be made
If I had even more time to work on this program I would like to separate out the 'formatting functionality' of the email, which is currently within the 'send_mail' method, under the Mailer class.  This would mean I could format the email and bring the elements of the data to be interpolated into the email, taking this responsibility away from the 'send_email' method. By separating these responsibilities also, testing would have been more accurate as it would possible to mock more elements to isolate the tests further.

I would have also separated out the unit tests and integration tests into separate files and create both for the 'Mailer' and  'payment_service' package also (I am still to test the payment_service).

The last addition to my code would be to include more exceptions ('Raise Errors') to ensure more edge-cases could be caught.
