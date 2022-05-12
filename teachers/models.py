from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    discipline = models.TextField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} - {self.discipline}'

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

