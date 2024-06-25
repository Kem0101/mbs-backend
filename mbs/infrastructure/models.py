from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class ElectoralRoll(models.Model):
    cedula = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_born = models.DateField()
    province = models.CharField(max_length=50)
    electoral_college = models.CharField(max_length=7)
    electoral_college_location = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.cedula} {self.first_name} {self.last_name} {self.date_born} {self.province} {self.electoral_college} {self.electoral_college_location}"


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_set')

    ROLE_CHOICES = (
        ('superadmin', 'Super Administrator'),
        ('coordinator', 'Coordinator'),
        ('facilitator', 'Facilitator')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    cedula = models.CharField(max_length=15, unique=True)
    cell_phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_born = models.DateField()
    province = models.CharField(max_length=50)
    electoral_college = models.CharField(max_length=7)
    electoral_college_location = models.CharField(max_length=100)
    username = models.CharField(max_length=150, blank=True, null=True)

    USERNAME_FIELD = 'cedula'
    REQUIRED_FIELDS = []
