from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('prewedding/', views.prewedding, name='prewedding'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]