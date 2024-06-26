import pytest
from mock import patch, MagicMock
from unittest.mock import patch, Mock
from main import User
from main import ZodiacCompatibility, User, Emailer


def test_valid_email():
    assert User("example@example.com").validate_email() is True
    assert User("user.name+tag+sorting@example.com").validate_email() is True
    assert User("user_name@example.co.uk").validate_email() is True


def test_invalid_email():
    assert User("plainaddress").validate_email() is False
    assert User("@missingusername.com").validate_email() is False
    assert User("username@.com").validate_email() is False


# Test ZodiacCompatibility
def test_load_configuration():
    with patch("os.getenv") as mock_getenv:
        mock_getenv.side_effect = lambda x: {
            "PRODUCTION_ENDPOINT": "http://api.example.com",
            "TWIN_FLAME_API": "secret_api_key",
        }.get(x)
        zodiac = ZodiacCompatibility()
        assert zodiac.api_url == "http://api.example.com"
        assert zodiac.headers["Authorization"] == "Bearer secret_api_key"
