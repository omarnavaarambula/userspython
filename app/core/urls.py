from django.urls import path
from . import views

urlpatterns = [
    path('/status', views.StatusView.as_view()),
    path('/file', views.FileUploadView.as_view()),
    path('/hello', views.hello_world),
    path('/register', views.RegisterView.as_view()),
    path('/login', views.LoginView.as_view()),
    path('/user', views.UserView.as_view()),
    path('/logout', views.LogoutView.as_view()),
]
