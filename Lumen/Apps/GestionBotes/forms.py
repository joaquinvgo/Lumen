from django import forms
from django.forms import inlineformset_factory
from Lumen.Apps.GestionBotes.models import Botes, Fotos
#from .validators import validate_file_extension
#from django.utils.html import format_html


class BotesForm(forms.ModelForm):

    class Meta:
        model=Botes
        fields=('Equipo','Pais','Agno','Carrera', 'Modalidad', 'PrecioVenta','CompradoA','FechaCompra','Observaciones','FotoPrincipal')
        

    def registrar_bote(self):
             
        nuevo_bote = Botes(Equipo=self.data['Equipo'],
                        Pais=self.data['Pais'],
                        Agno=self.data['Agno'],
                        Modalidad=self.data['Modalidad'],
                        PrecioVenta=self.data['PrecioVenta'],
                        CompradoA=self.data['CompradoA'],
                        FechaCompra=self.data['FechaCompra'],
                        Observaciones=self.data['Observaciones'],
                        FotoPrincipal=self.data['FotoPrinciapl'])
        nuevo_bote.save()
        return 'Registro correcto'

class ImageForm(forms.ModelForm):
    

    class Meta:
        model=Fotos
        fields=('bote','imagen')
      
        ImageFormSet=inlineformset_factory(Botes,Fotos,fields=('bote','imagen'),extra=3)

class FormularioContacto(forms.Form):
    
    asunto=forms.CharField(max_length=100, widget=forms.Textarea(attrs = {'cols': '40', 'rows': '2'}))
    email=forms.EmailField(widget=forms.Textarea(attrs = {'cols': '40', 'rows': '2'}))
    mensaje=forms.CharField(max_length=250, widget=forms.Textarea)
    pdffile=forms.FileField(required=False, widget=forms.FileInput(attrs={'accept':'image/*'}))
