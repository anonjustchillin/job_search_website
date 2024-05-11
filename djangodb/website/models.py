from django.db import models


# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Item(models.Model):
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
#
