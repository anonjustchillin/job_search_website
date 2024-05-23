from django.db import models
from users.models import User
from company.models import Company
from resume.models import Resume


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Job(models.Model):
    objects = models.Manager()

    type_choices = (
        ('Дистанційно', 'Дистанційно'),
        ('На місці', 'На місці'),
        ('Гібрид', 'Гібрид')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=20000)
    type = models.CharField(max_length=20, choices=type_choices, null=True, blank=True)
    reqs = models.TextField()

    is_available = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, null=True, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title


class ApplyJob(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
