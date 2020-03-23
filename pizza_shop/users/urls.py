from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView
from . import views
LoginView.template_name = 'users/login.html'
urlpatterns = [
    #登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #注销
    path('logout/', views.logout_view, name='logout'),
    #用户注册
    path('register/', views.register, name='register')
]
app_name = 'users'
