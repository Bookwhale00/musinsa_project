from django.urls import path
from user import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.user_logout, name='logout'),
]
