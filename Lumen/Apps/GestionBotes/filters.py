import django_filters

from Lumen.Apps.GestionBotes.models import Botes

class BotesFilter(django_filters.FilterSet):

	class Meta:
		model = Botes
		fields=['Agno','Equipo','Pais','Carrera', 'Modalidad']