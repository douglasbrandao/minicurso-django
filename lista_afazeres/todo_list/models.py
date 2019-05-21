from django.db import models

class ItemFazer(models.Model):
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.conteudo

    class Meta:
        verbose_name = 'Item a fazer'
        verbose_name_plural = 'Itens a fazer'
