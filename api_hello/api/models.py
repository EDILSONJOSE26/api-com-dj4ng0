# Create your models here.


from django.db import models

GENERO_CHOICES = [
    ('DRAMA', 'DRAMA'),
    ('COMEDIA', 'COMÉDIA'),
]


class Filme(models.Model):
    nome = models.CharField(max_length=8)
    genero = models.CharField(max_length=8,choices=GENERO_CHOICES)
    ano = models.PositiveIntegerField()
    duracao = models.PositiveIntegerField()

    