from django.db import models
from users.models import User


class Resume(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=30)
    location = models.CharField(max_length=50)

    upload_file = models.FileField(upload_to='resume', null=True, blank=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'
