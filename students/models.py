import random

from core.models import Person

from django.core.exceptions import ValidationError
from django.db import models

from groups.models import Group


class Student(Person):
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    class Meta:
        db_table = 'students'
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name} / ({self.phone_number})'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        groups = Group.objects.all()
        obj.group = random.choice(groups)
        obj.save()

    def clean(self):
        if self.group.student_count >= self.group.max_capacity:
            raise ValidationError('Sorry, this group is full already.')
