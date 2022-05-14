from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from faker import Faker

from teachers.validators import phone_number_validator


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name', validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, verbose_name='Last Name', validators=[MinLengthValidator(2)])
    discipline = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=20, null=True, validators=[phone_number_validator, MinLengthValidator(3)])

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} ({self.phone_number}) - {self.discipline}'

    @staticmethod
    def gen_teachers(cnt=10):
        fk = Faker()
        for _ in range(cnt):
            tchr = Teacher(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                age=fk.random_int(min=25, max=70),
                discipline=fk.job()
            )

            tchr.save()

