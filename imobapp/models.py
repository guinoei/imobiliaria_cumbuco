from django.db import models
from djmoney.models.fields import MoneyField
import string
import random

def gerar_codigo(tipo):
    codigo_prefixo = tipo[:2].upper()
    codigo_aleatorio = ''.join(random.choice(string.digits) for _ in range(4))
    return f"{codigo_prefixo}{codigo_aleatorio}"

class Propriedade(models.Model):
    finalidade_select = (
        ('Venda', 'Venda'),
        ('Aluguel', 'Aluguel'),
    )

    tipo_select = (
        ('Casa', 'Casa'),
        ('Flat', 'Flat'),
        ('Apartamento', 'Apartamento'),
        ('Cobertura', 'Cobertura'),
        ('Comercial', 'Comercial'),
    )

    titulo= models.CharField(max_length=100)
    finalidade= models.CharField(max_length=30, choices=finalidade_select)
    preco= MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    area_util= models.CharField(max_length=10, default=0)
    area_total= models.CharField(max_length=10, default="", blank=True)
    quartos= models.CharField(max_length=3, default=0)
    suites= models.CharField(max_length=3, blank=True)
    banheiros= models.CharField(max_length=10, default=0)
    vagas= models.CharField(max_length=3, default="", blank=True)
    descricao= models.TextField()
    tipo= models.CharField(max_length=50, choices=tipo_select)   
    foto1= models.ImageField(upload_to='static')
    foto2= models.ImageField(upload_to='static', blank=True)
    foto3= models.ImageField(upload_to='static', blank=True)
    foto4= models.ImageField(upload_to='static', blank=True)
    foto5= models.ImageField(upload_to='static', blank=True)
    foto6= models.ImageField(upload_to='static', blank=True)
    foto7= models.ImageField(upload_to='static', blank=True)
    foto8= models.ImageField(upload_to='static', blank=True)
    foto9= models.ImageField(upload_to='static', blank=True)
    foto10= models.ImageField(upload_to='static', blank=True)
    piscina= models.BooleanField(default=False)
    academia= models.BooleanField(default=False)
    quadra= models.BooleanField(default=False)
    churrasqueira= models.BooleanField(default=False)
    deck= models.BooleanField(default=False)
    rua= models.CharField(max_length=100)
    bairro= models.CharField(max_length=50)
    cidade= models.CharField(max_length=50)
    estado= models.CharField(max_length=50)
    slug= models.SlugField(default="", null=False)
    lat= models.DecimalField(max_digits=25, decimal_places=20, null=True, blank=True)
    lng= models.DecimalField(max_digits=25, decimal_places=20, null=True, blank=True)
    codigo = models.CharField(max_length=6, unique=True, blank=True, null=True)    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = gerar_codigo(self.tipo.__class__.__name__)
        super().save(*args, **kwargs)