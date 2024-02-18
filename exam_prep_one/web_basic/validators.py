from django.core.exceptions import ValidationError


def validate_username(value):
    for ch in value:
        if not ch.isdigit() and not ch.isalpha() and ch != "_":
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
