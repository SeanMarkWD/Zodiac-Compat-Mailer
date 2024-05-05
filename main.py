# Zodiac API Emailer
import requests
import os
import sys
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


class User:
    valid_zodiac_signs = [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces",
    ]

    def __init__(self, email):
        self.email = email
        # self.zodiac = zodiac

    def validate_email(self):
        # Validates if a user input email address is valid
        # Returns valid if True and invalid if False
        # Regex to check email validity
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return True
        return False

    # def validate_zodiac(self):
    #     # Zodiac verification
    #     return self.zodiac in User.valid_zodiac_signs

    # def is_valid(self):
    #     return self.validate_email() and self.validate_zodiac()


class ZodiacCompatibility:
    pass


class Emailer:
    # Email preparation
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(
        self, sender_email, receiver_email, sender_password, subject, content
    ):
        # Prepare the email content
        html = f"""
        <html>
        <body>
            <p>Hi,<br>
            This is a test Email
            </p>
        </body>
        </html>
        """
        part = MIMEText(html, "html")

        # Setup the MIME
        message = MIMEMultipart("alternative")
        message["Subject"] = "Your requested image"
        message["From"] = sender_email
        message["To"] = receiver_email
        message.attach(part)

        # Create SMTP session for sending the mail
        try:
            # Use Gmail's SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)  # Use 465 for SSL
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)  # Login with email and password

            # Convert the message to a string and send it
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Something went wrong... {e}")


# Error handling of email


def main():
    # 2CLI: Email + starsign
    sender_email = input("Enter your e-mail: ")
    user = User(sender_email)
    if user.validate_email():
        print("Valid email address")
        # break
    else:
        print("Invalid input. Please enter a valid email address.")


if __name__ == "__main__":
    main()
