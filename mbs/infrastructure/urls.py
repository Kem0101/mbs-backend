from django.urls import path
from mbs.infrastructure.views import index, UserCreateView, CedulaValidateView, UserLoginView

urlpatterns = [
    path('', index, name='index'),
    path('validate-cedula/', CedulaValidateView.as_view(), name='validate_cedula'),
    path('register', UserCreateView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login')
]
