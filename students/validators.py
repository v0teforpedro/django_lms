import datetime
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def phone_number_validator(phone_number):
    from .models import Student
    result = Student.objects.filter(phone_number=phone_number).exists()
    if result:
        raise ValidationError(f'Phone number {phone_number} is not unique.')


@deconstructible
class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, *args, **kwargs):
        age = datetime.date.today().year - args.year
        if age < self.age_limit:
            raise ValidationError(f'Age should be greater than {self.age_limit} y.o.')