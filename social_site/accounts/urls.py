from django.urls import path
from accounts.views import signup_view

urlpatterns = [
    path('iscriviti/', signup_view, name="signup_view"),
]
