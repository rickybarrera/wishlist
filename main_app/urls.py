from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.ItemCreate.as_view(), name ='add_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
]