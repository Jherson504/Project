from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('auth/', views.authenticate_user, name='authenticate-user'),
    path('auth/login/', views.login_user, name='login-user'),
    path('auth/logout/', views.logout_user, name='logout-user'),
    path('auth/sign-up/', views.sign_up_user, name='sign-up-user'),

]
