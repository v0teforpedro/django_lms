import datetime
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, *args, **kwargs):
        age = datetime.date.today().year - args[0].year
        if age < self.age_limit:
            raise ValidationError(f'Age should be greater than {self.age_limit} y.o.')