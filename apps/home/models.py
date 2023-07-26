from django.db import models

# Create your models here.
class home(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Home da TI'
        verbose_name_plural = 'Homes da TI'

    def __str__(self):
        return self.titulo