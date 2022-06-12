from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db import models

from teachers.models import Teacher


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        validators=[MinLengthValidator(4)]
    )
    max_capacity = models.PositiveSmallIntegerField(
        verbose_name='Maximum Capacity',
        validators=[MinValueValidator(10), MaxValueValidator(30)]
    )
    headman = models.OneToOneField(
        'students.Student',             # delayed import
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headman_group'
    )
    teachers = models.ManyToManyField(
        to=Teacher,
        blank=True,
        related_name='groups'
    )

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name} (capacity: {self.student_count}/{self.max_capacity})'

    @property
    def student_count(self):
        return self.students.count()
