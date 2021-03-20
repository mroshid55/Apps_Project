from django.urls import path, include

from .import views


urlpatterns = [
    path('SignUp', views.SIGNUP, name='SignUp'),
    path('Login', views.LOGIN, name='Login'),
    path('Logout', views.LOGOUT, name='Logout'),
    path('Pass_recovery', views.PASS_RECOVERY, name='Pass_recovery'),
    path('Profile', views.PROFILE, name='Profile'),
    path('Update_Profile/<str:pk>/', views.UPDATE_PROFILE, name='Update_Profile'),

]
