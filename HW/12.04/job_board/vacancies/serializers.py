from rest_framework import serializers
from .models import Vacancy

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
