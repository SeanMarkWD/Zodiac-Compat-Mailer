# Zodiac API Emailer
import requests

# Import necessary libraries
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

import sys
import re

# Import other modules or classes after loading the environment variables
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

    def __init__(self):
        self.api_url = os.getenv("PRODUCTION_ENDPOINT")
        self.headers = {
            "Authorization": f"Bearer {os.getenv('TWIN_FLAME_API')}",
            "Content-Type": "application/json",
        }

    def fetch_compatibility(self, sign, day="today"):
        """Fetch the zodiac compatibility information from the Aztro API."""
        data = {"sign": sign, "date": day}
        try:
            response = requests.post(self.api_url, headers=self.headers, json=data)
            response.raise_for_status()  # Raises a HTTPError for bad requests (4XX or 5XX)
            return response.json()  # Return the parsed JSON data
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")  # Print HTTP error message
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")  # General error catching
        return None

    def format_compatibility_data(data):
        """Format the compatibility data into a readable string."""
        if not data:
            return "No data available."

        # Extracting and formatting the compatibility data
        details = [
            f"Date: {data.get('current_date')}",
            f"Compatibility: {data.get('compatibility')}",
            f"Lucky Time: {data.get('lucky_time')}",
            f"Lucky Number: {data.get('lucky_number')}",
            f"Description: {data.get('description')}",
        ]
        return "\n".join(details)


class Emailer:
    # Email preparation
    def __init__(self):
        self.sender_email = os.getenv("EMAIL")
        self.sender_password = os.getenv("PASSWORD")

    def send_email(self, receiver_email, subject, content):
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
        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message.attach(part)

        # Create SMTP session for sending the mail
        try:
            # Use Gmail's SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)  # Use 465 for SSL
            server.starttls()  # Enable security
            server.login(
                self.sender_email, self.sender_password
            )  # Login with email and password

            # Convert the message to a string and send it
            text = message.as_string()
            server.sendmail(self.sender_email, receiver_email, message.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Something went wrong... {e}")


# Error handling of email


def main():
    # 2CLI: Email + starsign
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <email> <sign>")
        sys.exit(1)  # Exit the program indicating incorrect usage

    receiver_email = sys.argv[1]
    sign = sys.argv[2]
    zc = ZodiacCompatibility()
    compatibility_data = zc.fetch_compatibility(sign)
    if not compatibility_data:
        print("Failed to fetch compatibility data")
        sys.exit(1)
    print("Compatibility Result:", result)


if __name__ == "__main__":
    zc = ZodiacCompatibility()
    result = zc.fetch_compatibility("Gemini")
    print("Compatibility Result:", result)
