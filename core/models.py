import datetime

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from .validators import AdultValidator


class Person(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First Name',
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last Name',
        validators=[MinLengthValidator(2)]
    )
    birthday = models.DateField(
        default=datetime.date.today,
        validators=[AdultValidator(18)]
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        unique=True,
        validators=[MinLengthValidator(3)]
    )

    class Meta:
        abstract = True

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    @classmethod
    def _generate(cls):
        fk = Faker()
        obj = cls(
            first_name=fk.first_name(),
            last_name=fk.last_name(),
            birthday=fk.date_between(start_date='-60y', end_date='-20y'),
            phone_number=fk.phone_number()
        )
        obj.save()
        return obj

    @classmethod
    def generate(cls, cnt=10):
        for _ in range(cnt):
            cls._generate()
