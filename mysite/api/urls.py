from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.UserProfileListCreate.as_view(), name="UserProfileListCreate")
]
