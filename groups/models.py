from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        validators=[MinLengthValidator(4)]
    )
    subjects = models.CharField(
        max_length=100,
        verbose_name='Subject',
    )
    curr_students = models.PositiveSmallIntegerField(
        verbose_name='Current Capacity',
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    max_capacity = models.PositiveSmallIntegerField(
        verbose_name='Maximum Capacity',
        validators=[MinValueValidator(10), MaxValueValidator(30)]
    )

    def __str__(self):
        return f'{self.group_name} ( {self.curr_students} / {self.max_capacity} ): {self.subjects}'

    def clean(self):
        if self.curr_students > self.max_capacity:
            raise ValidationError('Amount of students in group exceeds its capacity.')
