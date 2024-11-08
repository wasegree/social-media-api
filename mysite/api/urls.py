from django.urls import path
from . import views

urlpatters = [
    path("user/", views.UserProfileListCreate.as_view(), name="UserProfileListCreate")
]
