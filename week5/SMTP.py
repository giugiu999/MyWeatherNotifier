"""
This module demonstrates how to send an email using Gmail SMTP in Python.
The email body includes weather information (fetched from Week 3 or mocked here).
https://myaccount.google.com/ to get the app password

Key Concepts:
1. **SMTP (Simple Mail Transfer Protocol)** – The standard protocol for sending emails.
2. **Gmail SMTP Server** – Gmail's server that receives email from your app and relays it to the recipient.
3. **MIME (Multipurpose Internet Mail Extensions)** – Defines the structure and encoding of email content.
4. **Authentication** – Verifying your Gmail account to ensure only authorized apps can send emails.

IMPORTANT:
- DO NOT hardcode sensitive information like passwords. 
- For now, placeholders are used; in Week 6, we will integrate `.env` files for security.
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Placeholder weather summary (could reuse get_weather from Week 3)
WEATHER_SUMMARY = "Today's weather in Beijing: 29°C, clear sky."

def create_email(sender_email, recipient_email, subject, body):
    """
    Composes an email message using MIME formatting.
    
    Parameters:
        sender_email (str): The Gmail address of the sender.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The main content of the email.
    
    Returns:
        MIMEMultipart: A formatted email object ready to be sent.
    """
    # MIME allows emails to have structured headers and bodies (text, HTML, attachments).
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    
    # Attach the body as plain text
    message.attach(MIMEText(body, "plain"))
    return message

def send_email(sender_email, app_password, recipient_email, subject, body):
    """
    Sends an email using Gmail's SMTP server.

    SMTP CONCEPT:
    - SMTP (Simple Mail Transfer Protocol) is how emails travel from your device to the recipient's mail server.
    - Gmail provides `smtp.gmail.com` as its SMTP gateway for outgoing emails.

    AUTHENTICATION:
    - Gmail no longer allows 'less secure apps'; you must use **App Passwords** generated in your account security settings.
    - Incorrect credentials or blocked "less secure apps" cause authentication errors.

    Parameters:
        sender_email (str): Your Gmail address.
        app_password (str): Your Gmail app password.
        recipient_email (str): Recipient email address.
        subject (str): Email subject.
        body (str): Email body.
    """
    # Step 1: Create the email with MIME formatting
    email_message = create_email(sender_email, recipient_email, subject, body)

    # Step 2: Connect to Gmail's SMTP server
    # Gmail uses smtp.gmail.com on port 587 (STARTTLS).
    # STARTTLS upgrades an insecure connection to an encrypted one.
    try:
        print("Connecting to Gmail SMTP server...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Upgrade the connection to encrypted mode
        print("Connected and secured via STARTTLS.")

        # Step 3: Authenticate with Gmail
        print("Logging in...")
        server.login(sender_email, app_password)  # Authentication
        print("Login successful.")

        # Step 4: Send the email
        print("Sending email...")
        server.sendmail(sender_email, recipient_email, email_message.as_string())
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your app password or Gmail settings.")
    except smtplib.SMTPConnectError:
        print("Failed to connect to the SMTP server.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Step 5: Close the connection
        server.quit()
        print("SMTP connection closed.")


if __name__ == "__main__":
    # Load credentials from environment variables
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    APP_PASSWORD = os.getenv("APP_PASSWORD")
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

    # Check if all required environment variables are set
    if not all([SENDER_EMAIL, APP_PASSWORD, RECIPIENT_EMAIL]):
        print("Error: Missing required environment variables. Please check your .env file.")
        print("Required variables: SENDER_EMAIL, APP_PASSWORD, RECIPIENT_EMAIL")
        exit(1)

    subject = "Weather Update"
    body = f"Hello,\n\n{WEATHER_SUMMARY}\n\nRegards,\nMyWeatherNotifier"
    send_email(SENDER_EMAIL, APP_PASSWORD, RECIPIENT_EMAIL, subject, body)
