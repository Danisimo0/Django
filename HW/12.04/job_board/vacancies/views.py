# Create your views here.
from rest_framework import viewsets
from .models import Vacancy
from .serializers import VacancySerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
