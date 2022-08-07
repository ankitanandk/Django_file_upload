from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_document, name='add_document'),
    path('send/', views.send_mail, name='send_mail'),
    path('delete/<int:pk>/', views.delete_document, name='delete_document'),
]
