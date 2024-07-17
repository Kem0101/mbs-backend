

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


class CedulaAuthBackend(ModelBackend):

    def authenticate(self, request, cedula=None, password=None, **kwargs):
        CustomUserModel = get_user_model()
        try:
            user = CustomUserModel.objects.get(cedula=cedula)
        except CustomUserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        CustomUserModel = get_user_model()
        try:
            return CustomUserModel.objects.get(pk=user_id)
        except CustomUserModel.DoesNotExist:
            return None
