from django.contrib import admin
#from django.db import models
#from django.forms import TextInput
from django.utils.html import format_html
from Lumen.Apps.GestionBotes.models import (Botes, Paises, Equipos, Fotos,Carreras, Modalidad)
from .forms import ImageForm
from django_admin_listfilter_dropdown.filters import ( 
    DropdownFilter, 
    ChoiceDropdownFilter, 
    RelatedDropdownFilter )
from django.contrib.admin.filters import (
    SimpleListFilter,
    AllValuesFieldListFilter,
    ChoicesFieldListFilter,
    RelatedFieldListFilter,
    RelatedOnlyFieldListFilter
)

# Register your models here.


class FotosAdmin(admin.ModelAdmin):
    list_display=("id","bote","imagen","fotos")
    #list_filter=['bote']
    search_fields=("id",)

    #Insertar la foto en list_display
    def fotos(self,obj):
        return format_html('<img src={} width=80 height=120 />',obj.imagen.url)

class FotosInline(admin.TabularInline):
    #permite mostrar las rutas de las fotos en los botes, sólo cuando se editan, no cuando se listan
    #ello se consigue luego añadiendo en BotesAdmin inline=[FotosInline]
    model=Fotos
    form=ImageForm
    extra=3
       

class BotesAdmin(admin.ModelAdmin):
    #Filtro de la página de administracion
    
    list_display=("id","Carrera","Equipo","Pais","Agno")
    
    inlines=[FotosInline]
        
    list_filter = [
        # for ordinary fields
        ('Agno', DropdownFilter),
        # for choice fields
        #('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('Equipo', RelatedDropdownFilter),
        ('Pais', RelatedDropdownFilter),
        ('Carrera', RelatedDropdownFilter),
        ('Modalidad', RelatedDropdownFilter),
        
    ]
    search_fields=('Agno','CompradoA','Equipo__Nombre__icontains',
    'Pais__Nombre__icontains','Carrera__Nombre__icontains','Modalidad__Nombre__icontains',)
    

""" class EntityAdmin(admin.ModelAdmin):
    
    list_filter = [
        # for ordinary fields
        #('Agno', DropdownFilter),
        # for choice fields
        #('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('Equipo', RelatedDropdownFilter),
        ('Carrera', RelatedDropdownFilter),
        ('Pais', RelatedDropdownFilter),
    ]

    class Meta:
        model=Botes """


""" class CustomFilter(SimpleListFilter):
    title='Agno'
    parameter_name='Agno'
    template = 'django_admin_listfilter_dropdown/dropdown_filter.html'

    def lookups(self, request, model_admin):
        return (request)

    def queryset(self, request, queryset):
        return queryset """
        


admin.site.register(Botes, BotesAdmin)
admin.site.register(Paises)
admin.site.register(Carreras)
admin.site.register(Equipos)
admin.site.register(Modalidad)
admin.site.register(Fotos, FotosAdmin)
#admin.site.register(EntityAdmin, CustomFilter)