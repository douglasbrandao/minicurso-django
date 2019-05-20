from django.db import models

class Aluno(models.Model):
   ECO = 'ECO'
   ECA = 'ECA'
   SPI = 'SPI'
   TUR = 'TUR'

   CURSO_ESCOLHAS = (
       (ECO, 'Engenharia de Computação'),
       (ECA, 'Eng. de Controle e Automação'),
       (SPI, 'Sistemas para internet'),
       (TUR, 'Turismo')
   )

   nome = models.CharField(max_length=256)
   idade = models.IntegerField()
   curso = models.CharField(max_length=3, choices=CURSO_ESCOLHAS, default=ECO)

   def __str__(self):
       return self.nome

class Servidor(models.Model):
    SRV = 'SRV'
    PRF = 'PRF'

    SERVIDOR_ESCOLHAS = (
        (SRV, 'Servidor'),
        (PRF, 'Professor')
    )

    nome = models.CharField(max_length=256)
    cargo = models.CharField(max_length=3, choices=SERVIDOR_ESCOLHAS, default=SRV)
    contratacao = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Servidores'
