from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticias/<int:id>/', views.news_detail, name='news_detail'),
    path('codigo-social/', views.codigo_social, name='codigo_social'), # Adicione esta linha
]