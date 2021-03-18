from django.urls import path, include

from .import views


urlpatterns = [
    path('', views.NOTES, name='Notes'),
    path('Update_Notes/<str:pk>/', views.UPDATE_NOTES, name='Update_Notes'),
    path('Delete_Notes/<str:pk>/', views.DELETE_NOTES, name='Delete_Notes'),

]
