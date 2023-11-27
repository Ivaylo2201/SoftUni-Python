from django.core.exceptions import ValidationError
import re


def validate_name(value: str) -> None:
    for ch in value:
        if not (ch.isalpha() or ch.isspace()):
            raise ValidationError("Name can only contain letters and spaces")


def validate_phone_number(value: str) -> None:
    if not re.match("\+359\d{9}", value):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
