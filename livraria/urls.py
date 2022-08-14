from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('osoutros', views.osoutros, name='osoutros'),
    
    path('livros', views.livros, name='livros'),  
    path('livros/criarLivro', views.criarLivro, name='criarLivro'),
    path('livros/editarLivro', views.editarLivro, name='editarLivro'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('livros/editarLivro/<int:id>', views.editarLivro, name='editarLivro'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


