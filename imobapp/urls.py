from django.urls import path
from imobapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("propriedade_detalhe/<slug:slug>", views.propriedade_detalhe, name="propriedade_detalhe"),
         
]