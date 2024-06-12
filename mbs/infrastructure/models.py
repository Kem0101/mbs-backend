from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ElectoralRoll(models.Model):
    cedula = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_born = models.DateField()
    province = models.CharField(max_length=50)
    electoral_college = models.CharField(max_length=7)
    electoral_college_location = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.cedula} {self.name} {self.lastname}"


class User(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Administrator'),
        ('coordinator', 'Coordinator'),
        ('facilitator', 'Facilitator')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    cedula = models.CharField(max_length=15, unique=True)
    date_born = models.DateField()
    province = models.CharField(max_length=50)
    electoral_college = models.CharField(max_length=7)
    electoral_college_location = models.CharField(max_length=100)
