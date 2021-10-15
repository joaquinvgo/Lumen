from django.shortcuts import render, redirect
from django.core.paginator import Paginator
#from django.http import HttpResponse
#from django.views.generic import CreateView, TemplateView
#from django.urls import reverse_lazy
from Lumen.Apps.GestionBotes.filters import BotesFilter
from django.core.mail import EmailMessage
# from django.conf import settings
from django.db.models import Q
#from django_admin_listfilter_dropdown.filters import ( 
#    DropdownFilter, 
#    ChoiceDropdownFilter, 
#    RelatedDropdownFilter )
#from django.contrib.admin.filters import (
#    SimpleListFilter,
#    AllValuesFieldListFilter,
#    ChoicesFieldListFilter,
#    RelatedFieldListFilter,
#    RelatedOnlyFieldListFilter)

#from django.db.models.fields import BLANK_CHOICE_DASH
#from .admin import FotosAdmin
from Lumen.Apps.GestionBotes.forms import BotesForm, FormularioContacto
from Lumen.Apps.GestionBotes.models import Botes, Fotos, Carreras, Equipos, Paises

# Create your views here.


def about(request):
    return render(request, 'about.html')


def bienvenido(request):
    return render(request, 'home.html')
    
def muestrabotes(request):
    zoom=2
    queryset=request.GET.get("buscar")
    print(queryset)
    if queryset:
        botes = Botes.objects.filter(Q(Pais__Nombre__icontains = queryset)|
        Q(Carrera__Nombre__icontains = queryset)|
        Q(Equipo__Nombre__icontains = queryset)|
        Q(Agno__icontains = queryset)|
        Q(Observaciones__icontains = queryset)).distinct().order_by('Agno')
    else:
        botes =Botes.objects.filter().order_by('Agno')

    fotos = Fotos.objects.all()
    mifiltro = BotesFilter(request.GET, queryset = botes)
    print(mifiltro,mifiltro.qs)
   
    page = request.GET.get('page',1)
    paginator = Paginator(mifiltro.qs,6)
    page_range = paginator.get_elided_page_range(number=page)
    botes = paginator.get_page(page)
    
    
    context=request.GET
    ancho=80*zoom
    alto=107*zoom
    params = {'botes': botes, 'fotos':fotos,'ancho':ancho,'alto':alto,
    'filter':mifiltro,'botes': botes, 'paginator': paginator, 
    'page_number': page, 'page_range': page_range, 'context': context, "zoom": zoom,"queryset": queryset}
    return render(request, 'muestrabotes.html',params)
  

def indice(request):
    register_form =BotesForm() 

    if request.method=='POST':
                
        if register_form.is_valid():
            register_form.save()
            return redirect('muestrabotes')
    
    return render(request, 'mi_form.html',{'register_form': register_form})


def contacto(request):

    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST, request.FILES)

        if miFormulario.is_valid():
            
            infForm=miFormulario.cleaned_data
            
            msg = EmailMessage(infForm['asunto'],  infForm['mensaje'], infForm['email'], ['joaquin@villadiego.es'])
            msg.content_subtype = "html"
                      
            try:
                myattach=request.FILES['pdffile']
                msg.attach(myattach.name,myattach.read(),myattach.content_type)
            except:
                print('No se adjunta ningún archivo')
                
            msg.send()
            return render(request,"gracias.html")

    else:
        asunto=request.GET['Asunto']
        miFormulario=FormularioContacto(initial={'asunto':asunto})
        

    return render(request, 'formulario_contacto.html', {'form':miFormulario})