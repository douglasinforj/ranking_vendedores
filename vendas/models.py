from django.db import models

class Venda(models.Model):
    usuario = models.CharField(max_length=255)
    total_vendas = models.IntegerField()
    horario = models.TimeField()


    def __str__(self):
        return f"{self.usuario} - {self.total_vendas} vendas"
