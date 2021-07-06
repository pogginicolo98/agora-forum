from django.urls import path
from forum import views

urlpatterns = [
    path('new-section/', views.NewSection.as_view(), name='new_section'),
    path('delete-section/<int:pk>/', views.DeleteSection.as_view(), name='delete_section'),
    path('section/<int:pk>/', views.section_view, name='section_view'),
    path('section/<int:pk>/new-discussion/', views.new_discussion, name='new_discussion'),
    path('discussion/<int:pk>/', views.discussion_view, name='discussion_view'),
    path('discussion/<int:pk>/reply/', views.reply, name='reply'),
    path('discussion/<int:id>/delete-post/<int:pk>/', views.DeletePost.as_view(), name='delete_post'),
]
