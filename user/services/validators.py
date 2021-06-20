from django.core.validators import RegexValidator
from django.conf import settings
from django.core.exceptions import ValidationError

validate_phone = RegexValidator(
    regex=r"^998\d{9}$",
    message="Phone number must begin with 998 and contain only 12 numbers",
)


def validate_file_type_gallery(value):
    file = value.name.upper()
    if not file.endswith(settings.IMAGE_TYPES + settings.VIDEO_TYPES):
        raise ValidationError('File type not supported. JPG, JPEG, PNG, MP4 or MPEG recommended.')


def validate_image_type(value):
    file = value.name.upper()
    if not file.endswith(settings.IMAGE_TYPES):
        raise ValidationError('File type not supported. JPG, JPEG or PNG recommended.')
