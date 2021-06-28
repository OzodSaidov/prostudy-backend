from django.conf import settings
from django.core.exceptions import ValidationError
import re


def validate_phone(value):
    pattern = r"^\+?998\d{9}$"
    if not re.search(pattern, str(value)):
        raise ValidationError('Phone number must begin with 998 and contain only 12 numbers')


def validate_file_type(value):
    file = value.name.upper()
    if not file.endswith(settings.IMAGE_TYPES + settings.VIDEO_TYPES):
        raise ValidationError('File type not supported. JPG, JPEG, PNG, MP4 or MPEG recommended.')


def validate_image_type(value):
    file = value.name.upper()
    if not file.endswith(settings.IMAGE_TYPES):
        raise ValidationError('File type not supported. JPG, JPEG or PNG recommended.')
