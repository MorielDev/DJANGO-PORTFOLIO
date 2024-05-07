from django.urls import path
from . import views
from .views import create_portfolio, portfolio_detail, success_page
urlpatterns = [
    path('', views.create_portfolio, name= 'create_portfolio'),
    path('portfolio/<int:id>/', portfolio_detail, name='portfolio_detail'),
    path('success/', success_page, name='success_page')
]

    
    