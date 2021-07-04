from django.urls import path
from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('users/', views.UsersList.as_view(), name='user_list'),
    path('user/<slug:username>/', views.user_profile_view, name='user_profile'),
    path('cerca/', views.cerca, name='funzione_cerca'),
]
