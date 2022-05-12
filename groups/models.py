from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    max_capacity = models.PositiveIntegerField()
    curr_students = models.PositiveIntegerField()
    disciplines = models.TextField()

    def __str__(self):
        return f'{self.group_name} ( {self.curr_students} / {self.max_capacity} ) - {self.disciplines}'
