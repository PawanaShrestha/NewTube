from . import views
from django.urls import path

urlpatterns = [
    path('login_user/', views.login_user, name = "login"),
    path('logout_user/', views.logout_user, name = "logout"),
    path('register_user/', views.register_user, name = "register_user"),
    path('user_profile/', views.user_profile, name = "user_profile"),
    path('edit_user_profile/', views.edit_user_profile, name = "edit_user_profile"),
]