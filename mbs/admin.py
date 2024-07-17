from django.contrib import admin
from mbs.infrastructure.models import CustomUser, ElectoralRoll

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(ElectoralRoll)
