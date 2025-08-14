import smtplib
from email.mime.text import MIMEText
import os
import logging

def send_email(to_email, subject, body):
    """
    Send a plaintext email via Gmail SMTP.

    Wrapped in try/except to provide friendly, beginner-focused messages.
    """
    from_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    if not from_email or not password:
        # try/except helps programs fail gracefully with clear messages.
        raise ValueError("EMAIL_ADDRESS and EMAIL_PASSWORD environment variables must be set")

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        logging.info(f"Sending email to {to_email}...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        logging.info(f"Email sent successfully to {to_email}")
        return True
    except smtplib.SMTPAuthenticationError:
        logging.error("Email authentication failed — check EMAIL_ADDRESS and EMAIL_PASSWORD (app password).")
    except smtplib.SMTPConnectError:
        logging.error("Could not connect to SMTP server — check your internet connection.")
    except Exception as e:
        logging.error(f"Error sending email: {e}")
    return False
