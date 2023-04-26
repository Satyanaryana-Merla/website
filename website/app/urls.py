"""importing path"""
from django.urls import path
from app import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('store', views.store, name='store'),
    # path('about', views.about, name='about'),
    path('index', views.index, name='index'),
    path('products', views.products, name='products')
]
