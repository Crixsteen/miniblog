from django.urls import path
from . import views  # Importiamo le viste dalla cartella 'blog'

urlpatterns = [
    path('', views.home, name='home'),  # Pagina principale
    path('posts/', views.post_list, name='post_list'),  # Lista dei post
    path('destinazioni/', views.destinazioni, name='destinazioni'),  # Pagina Destinazioni
]



