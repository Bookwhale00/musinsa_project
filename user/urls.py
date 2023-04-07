from django.urls import path
from user import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]
