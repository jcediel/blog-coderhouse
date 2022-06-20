from django.urls import path

from user import views


app_name='user'
urlpatterns = [
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('signup', views.register, name='user-register'),
    path('signup/update', views.user_update, name='user-update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
]
