from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    max_capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(10), MaxValueValidator(30)])
    curr_students = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    disciplines = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.group_name} ( {self.curr_students} / {self.max_capacity} ) - {self.disciplines}'
