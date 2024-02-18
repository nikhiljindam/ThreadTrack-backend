from django.urls import path
from authentication import views


urlpatterns = [
    path("login", views.Login.as_view(), name="token_obtain_pair"),
    path("logout", views.Logout, name="token_refresh"),
]
