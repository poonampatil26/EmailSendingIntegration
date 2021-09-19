from django.urls import path
from .views import sendEmailView

urlpatterns = [
    path('email/',sendEmailView),
]
