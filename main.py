# Zodiac API Emailer
import requests
import os
import sys
import re
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

    def __init__(self, email, zodiac):
        self.email = email
        self.zodiac = zodiac

    def validate_email(self):
        # Validates if a user input email address is valid
        # Returns valid if True and invalid if False
        # Regex to check email validity
        if re.match(r"[^@]+@[^@]+\.[^@]+"):
            return True
        return False

    def validate_zodiac(self):
        # Zodiac verification
        return self.zodiac in User.valid_zodiac_signs

    def is_valid(self):
        return self.validate_email() and self.validate_zodiac()


class ZodiacCompatibility:
    pass


class Emailer:
    def __init__(self, sender_emailer, sender_password):
        pass


# 2CLI: Email + starsign


# Email preparation


# Error handling of email
