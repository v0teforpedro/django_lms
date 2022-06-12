from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models

from groups.models import Group


class Course(models.Model):
    course_name = models.CharField(
        max_length=50,
        verbose_name='Course name',
        validators=[MinLengthValidator(3)]
    )
    hours = models.PositiveSmallIntegerField(
        verbose_name='Course hours',
        validators=[MinValueValidator(20), MaxValueValidator(100)]
    )
    group = models.OneToOneField(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='group_course'
    )

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'{self.course_name}'
