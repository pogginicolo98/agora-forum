from django.urls import path
from accounts.views import signup_view

urlpatterns = [
    path('signup/', signup_view, name="signup_view"),
]
