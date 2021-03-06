from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register'),
    path('users/profile/', views.getUserProfile, name='users-profile'),
    path('users/', views.getUsers, name='users'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>/', views.getProduct, name='product'),
]
