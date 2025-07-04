from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')  # Make sure it's set

# Helper function to send email using SendGrid
def send_sendgrid_email(subject, body, to_email):
    if not SENDGRID_API_KEY:
        print("SendGrid API Key is not set.")
        return False

    message = Mail(
        from_email=os.environ.get("DEFAULT_FROM_EMAIL"),  # Use your SendGrid verified email
        to_emails=to_email,
        subject=subject,
        html_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"SendGrid response: {response.status_code}, {response.body}")
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False