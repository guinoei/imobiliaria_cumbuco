from django.contrib import admin
from .models import Propriedade


@admin.register(Propriedade)

class PropriedadeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("finalidade", "tipo", "bairro", "cidade", "area_util")}