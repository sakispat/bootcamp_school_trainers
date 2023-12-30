from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('trainer/create/', views.create_trainer, name='create_trainer'),
    path('trainer/edit/<int:trainer_id>/', views.update_trainer, name='update_trainer'),
    path('trainer/delete/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
    path('search/', views.search_trainer, name='search'),
]
