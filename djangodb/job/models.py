from django.db import models
from users.models import User
from company.models import Company


class Job(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=20000)
    type = models.CharField(max_length=50)
    reqs = models.TextField()
    is_available = models.BooleanField(default=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
