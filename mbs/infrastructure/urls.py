from django.urls import path
from mbs.infrastructure.views import index, UserRepositoryView

urlpatterns = [
    path('', index, name='index'),
    path('register', UserRepositoryView.as_view(), name='register')
]
