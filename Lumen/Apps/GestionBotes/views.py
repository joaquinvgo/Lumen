from django.shortcuts import render, redirect
from django.core.paginator import Paginator
#from django.http import HttpResponse
#from django.views.generic import CreateView, TemplateView
#from django.urls import reverse_lazy
from Lumen.Apps.GestionBotes.filters import BotesFilter
from django.core.mail import EmailMessage
# from django.conf import settings
#from django.db.models import Q
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
from Lumen.Apps.GestionBotes.models import Botes, Fotos
# Create your views here.


def about(request):
    return render(request, 'about.html')


def bienvenido(request):
    return render(request, 'home.html')
    
def muestrabotes(request):
    zoom=2
    botes = Botes.objects.filter().order_by('Agno')
    fotos = Fotos.objects.all()
    mifiltro = BotesFilter(request.GET, queryset = botes)
    paginator=Paginator(mifiltro.qs,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        zoom=float(request.POST['zoom'])
    except:
        zoom=zoom
    context=request.GET
    ancho=80*zoom
    alto=160*zoom
    params = {'botes': botes, 'fotos':fotos,'ancho':ancho,'alto':alto,
    'filter':mifiltro,'page_obj': page_obj, 'paginator': paginator, 
    'page_number': page_number, 'context': context, "zoom": zoom}
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