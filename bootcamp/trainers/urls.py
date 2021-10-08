from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_trainer, name='create'),
    path('edit/<int:id>/', views.edit_trainer, name='edit'),
    path('delete/<int:id>/', views.delete_trainer, name='delete'),
    path('search/', views.search_trainer, name='search'),
]

