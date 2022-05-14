import datetime
from django.core.exceptions import ValidationError


ADULT_AGE_LIMIT = 18


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < ADULT_AGE_LIMIT:
        raise ValidationError('Age should be greater than 18 y.o.')


def phone_number_validator(phone_number):
    from .models import Student
    result = Student.objects.filter(phone_number=phone_number).exists()
    if result:
        raise ValidationError(f'Phone number {phone_number} is not unique.')