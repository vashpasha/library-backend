from django.urls import path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView

from .views import UserDetailAPI, UserListAPI

urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('users/', UserListAPI.as_view()),
    path('profile/', UserDetailAPI.as_view(), name='profile'),
]