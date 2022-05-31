from core.models import Person

from django.db import models

from faker import Faker


class Teacher(Person):
    subject = models.CharField(
        max_length=100,
        verbose_name='Subject'
    )

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.phone_number}): {self.subject}'

    @classmethod
    def _generate(cls):
        fk = Faker()
        obj = super()._generate()
        obj.subject = fk.job()
        obj.save()
