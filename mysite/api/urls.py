from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.UserProfileListCreate.as_view(), name="UserProfileListCreate"),
    path(
        "user/<int:pk>",
        views.UserProfileRetrieveUpdateDestroy.as_view(),
        name="UserProfileRetrieveUpdateDestroy",
    ),
]
