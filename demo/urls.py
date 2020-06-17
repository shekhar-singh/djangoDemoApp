from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.index, name='index'),
    path('', views.new_detail, name='new_detail'),
]