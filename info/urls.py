from django.urls import path
from . import views

urlpatterns = [
    path('', views.me, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
