from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.template import loader
from .models import Propriedade
from django.conf import settings


def home(request):
    qs = Propriedade.objects.all()
    buscar_finalidade_query = request.GET.get('buscar_finalidade')
    buscar_tipo_query = request.GET.get('buscar_tipo')
    buscar_cidade_query = request.GET.get('buscar_cidade')
    buscar_bairro_query = request.GET.get('buscar_bairro')
    buscar_banheiros_query = request.GET.get('buscar_banheiros')
    buscar_quartos_query = request.GET.get('buscar_quartos')
    if buscar_finalidade_query != '' and buscar_finalidade_query is not None:
        qs = qs.filter(Q(finalidade__icontains=buscar_finalidade_query)).distinct
    elif buscar_tipo_query != '' and buscar_tipo_query is not None:
        qs = qs.filter(Q(tipo__icontains=buscar_tipo_query)).distinct
    elif buscar_cidade_query != '' and buscar_cidade_query is not None:
        qs = qs.filter(Q(cidade__icontains=buscar_cidade_query)).distinct
    elif buscar_bairro_query != '' and buscar_bairro_query is not None:
        qs = qs.filter(Q(bairro__icontains=buscar_bairro_query)).distinct
    elif buscar_banheiros_query != '' and buscar_banheiros_query is not None:
        qs = qs.filter(Q(banheiros__icontains=buscar_banheiros_query))
    elif buscar_quartos_query != '' and buscar_quartos_query is not None:
        qs = qs.filter(Q(quartos__icontains=buscar_quartos_query))
    context = {
        'queryset': qs
    }
    return render(request, 'home.html', context)


# def propriedade_detalhe(request, slug):
#     propriedade = Propriedade.objects.get(slug=slug)
#     # propriedade_detalhe = Propriedade.objects.get()
#     template = loader.get_template('propriedade_detalhe.html')
#     enderecos = list(Propriedade.objects.values('lat', 'lng', 'slug')) 
#     context = {
#         'propriedade_detalhe': propriedade,
#         'enderecos': enderecos,
#         }
#     return HttpResponse(template.render(context, request))


def propriedade_detalhe(request, slug):
    propriedade = Propriedade.objects.get(slug=slug)
    template = loader.get_template('propriedade_detalhe.html')
    localizacao = [propriedade.lat, propriedade.lng]
    context = {
        'propriedade_detalhe': propriedade,
        'localizacao': localizacao,      
        }
    return HttpResponse(template.render(context, request))