import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from main import User


def test_valid_email():
    assert User("example@example.com").validate_email() is True
    assert User("user.name+tag+sorting@example.com").validate_email() is True
    assert User("user_name@example.co.uk").validate_email() is True


def test_invalid_email():
    assert User("plainaddress").validate_email() is False
    assert User("@missingusername.com").validate_email() is False
    assert User("username@.com").validate_email() is False
