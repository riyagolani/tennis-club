from django.urls import path
from members import views

urlpatterns = [
    # Accessible to all
    path('', views.homePage, name='home'),
    path('members/', views.members, name='members'),
    path('members/details/<username>', views.details, name='details'),
    # Register
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # Only accessible to member
    path('home/<username>', views.memberHome, name='memberhome'),
]