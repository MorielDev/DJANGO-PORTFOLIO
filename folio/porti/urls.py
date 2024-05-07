from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_portfolio, name= 'create_portfolio')
]
