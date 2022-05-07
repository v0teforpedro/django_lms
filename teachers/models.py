from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    discipline = models.TextField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} {self.discipline}'
