from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # show welcome first
    path('login/', views.login_view, name='login'),
    path('restaurant/dashboard/', views.restaurant_dashboard, name='restaurant-dashboard'),
    path('volunteer/dashboard/', views.volunteer_dashboard, name='volunteer-dashboard'),
]