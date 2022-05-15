import datetime
from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker
from core.validators import AdultValidator
from .validators import phone_number_validator


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name', validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, verbose_name='Last Name', validators=[MinLengthValidator(2)])
    age = models.PositiveSmallIntegerField()
    birthday = models.DateField(default=datetime.date.today, validators=[AdultValidator(18)])
    phone_number = models.CharField(max_length=20, null=True, validators=[phone_number_validator, MinLengthValidator(3)])

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} / ({self.phone_number})'

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    @staticmethod
    def gen_students(cnt=10):
        fk = Faker()
        for _ in range(cnt):
            result = Student(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                age=fk.random_int(min=18, max=45),
                birthday=fk.date_between(start_date='-65', end_date='-15y'),  # почему фэйкер не хочет работать с этим полем?
                phone_number=fk.phone_number()
            )
            result.save()
