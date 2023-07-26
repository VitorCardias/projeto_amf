from django.db import models

# Create your models here.
class Home(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='home', null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Home da TI'
        verbose_name_plural = 'Homes da TI'

    def __str__(self):
        return self.titulo