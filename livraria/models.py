from django.db import models

# Create your models here.
class livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    imagem = models.ImageField(upload_to='imagens/',verbose_name='Imagem',null=True)
    descricao = models.TextField(null=True, verbose_name='Descricao')
    
    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descrição: " + self.descricao
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagem.storage.delete(self.imagem.name)
        super().delete()
        
    