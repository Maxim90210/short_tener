from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_id>/', views.redirect_url, name='redirect_url'),
]
