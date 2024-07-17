
from django.conf import settings
from rest_framework.authtoken.models import Token

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_set')

    username = None

    ROLE_CHOICES = (
        ('superadmin', 'Super Administrator'),
        ('coordinator', 'Coordinator'),
        ('facilitator', 'Facilitator'),
        ('member', 'Member')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    cedula = models.CharField(max_length=15, unique=True)
    cell_phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_born = models.DateField()
    province = models.CharField(max_length=50)
    electoral_college = models.CharField(max_length=7)
    electoral_college_location = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_users')

    USERNAME_FIELD = "cedula"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.cedula


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


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
